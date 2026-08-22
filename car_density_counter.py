"""
Multi-video, multi-intersection vehicle counting.
====================================================

WHAT THIS SCRIPT DOES
----------------------
This script processes MULTIPLE dashcam/traffic videos in one run. For each
video, you define a "detection zone" (a region of the frame to look for
vehicles in) and a list of "intersections" -- individual turns/events within
that video, each with:

    - a "pre" phase  (optional): a timeframe just before the turn happens
    - a "true" phase (required): the timeframe of the turn itself

For every (intersection, phase) pair, the script:
    1. Runs a YOLO vehicle detector (car / motorcycle / bus / truck) on every
       frame in that timeframe.
    2. Counts how many detected vehicles fall inside the detection zone.
    3. Records the MAX count seen, and saves the annotated frame it occurred
       on.
    4. Records the MEDIAN count across all frames in that timeframe, and
       saves the annotated frame closest to that median (for a visual
       sanity check).

Only frames covered by at least one timeframe are ever run through the
detector -- frames outside every window are skipped, so you don't pay
detection cost for footage you don't care about.

PROJECT FILES
-------------
    vehicle_counter.py      <- this file (the engine). Contains a small
                                EXAMPLE configuration below so you can see
                                the expected format and test the pipeline.
    intersection_config.py  <- the full production configuration (every
                                participant/video/turn in the actual study).
    README.md                <- setup instructions, how resume mode works,
                                output structure, and known data caveats.

HOW TO RUN THE FULL STUDY (not just the example)
--------------------------------------------------
Replace the EXAMPLE VIDEOS dict below with:

    from intersection_config import VIDEOS

then run this file as normal. See README.md for full details.

RESUME SUPPORT
---------------
If a run gets interrupted partway through (e.g. a network drive
disconnects), you don't need to start over. Each video that finishes
successfully gets a "_DONE.marker" file in its output folder. On the next
run, any video with that marker is skipped automatically, and its previous
results are reused when building the combined summary CSV. Only videos that
didn't finish (no marker) get reprocessed. See README.md for details.
"""

import statistics
import re
from pathlib import Path

import cv2
from ultralytics import YOLO

# ---------------------------------------------------------------------------
# BASIC CONFIG
# ---------------------------------------------------------------------------
OUTPUT_DIR = Path("intersection_outputs")

# Set this True only when you want a totally fresh run that wipes everything,
# including videos that already finished successfully in a previous run.
# Leave False (default) to resume a run that got cut off partway through --
# already-completed videos will be skipped rather than reprocessed.
CLEAR_OUTPUT_DIR_EACH_RUN = False

# When True (default), a video whose output folder already has a completion
# marker from a prior run is skipped instead of being reprocessed.
RESUME_MODE = True

VERBOSE_PER_DETECTION = False  # set True for a per-frame, per-box print log

# COCO class IDs used by the YOLO model, restricted to vehicle classes.
VEHICLE_CLASSES = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
}

if CLEAR_OUTPUT_DIR_EACH_RUN and OUTPUT_DIR.exists():
    for old_file in OUTPUT_DIR.rglob("*"):
        if old_file.is_file():
            old_file.unlink()
OUTPUT_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------------------------
# VIDEO CONFIGURATION -- EXAMPLE ONLY
# ---------------------------------------------------------------------------
# This is a minimal example showing the expected structure for VIDEOS:
#
#   - top-level key   -> a short, unique name for this video (used to name
#                         its output folder and its rows in the summary CSV)
#   - "video_path"    -> full path to the video file on disk. Leave as ""
#                         to skip this video entirely (it will be reported
#                         as skipped, not processed).
#   - "zone"          -> the detection zone, as fractions (0.0-1.0) of the
#                         frame's width/height. The zone is a "plus sign"
#                         shape: a vertical strip spanning the full frame
#                         height between vert_left/vert_right, and a
#                         horizontal strip spanning the full frame width
#                         between hor_top/hor_bottom. A detection counts if
#                         its center falls in EITHER strip. Setting all four
#                         values to 0.0/1.0 (as below) makes the zone cover
#                         the entire frame.
#   - "intersections" -> a list of turns/events to analyze in this video.
#                         Each has a "name", an optional "pre" timeframe,
#                         and a required "true" timeframe. Timestamps use
#                         the format "M:SS:MMM" (minutes:seconds:millis),
#                         e.g. "2:08:082" = 2 minutes, 8.082 seconds.
#                         Set "pre" to None if there's no pre-turn data for
#                         that intersection.
#
# To run the real dataset instead of this example, comment out the VIDEOS
# dict below and uncomment the import line underneath it.

VIDEOS = {
    "EXAMPLE_VIDEO_1": {
        "video_path": "",  # <-- fill in a real path to try this out
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "EXAMPLE_VIDEO_1_TurnA",
                "pre":  {"start": "0:03:333", "end": "0:13:333"},
                "true": {"start": "0:13:333", "end": "0:18:000"},
            },
            {
                "name": "EXAMPLE_VIDEO_1_TurnB",
                "pre":  None,  # no pre-turn data available for this one
                "true": {"start": "1:05:000", "end": "1:20:500"},
            },
        ],
    },
}

# from intersection_config import VIDEOS  # <-- uncomment to run the real dataset


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def zone_to_pixels(zone_frac, width, height):
    """Convert a fractional zone definition into pixel bounds for one frame."""
    return {
        "vert_left": int(width * zone_frac["vert_left"]),
        "vert_right": int(width * zone_frac["vert_right"]),
        "vert_top": 0,
        "vert_bottom": height,
        "hor_left": 0,
        "hor_right": width,
        "hor_top": int(height * zone_frac["hor_top"]),
        "hor_bottom": int(height * zone_frac["hor_bottom"]),
    }


def is_in_zone(cx, cy, zpx):
    """True if the point (cx, cy) falls inside the vertical or horizontal strip."""
    in_vertical = zpx["vert_left"] <= cx <= zpx["vert_right"] and zpx["vert_top"] <= cy <= zpx["vert_bottom"]
    in_horizontal = zpx["hor_left"] <= cx <= zpx["hor_right"] and zpx["hor_top"] <= cy <= zpx["hor_bottom"]
    return in_vertical or in_horizontal


def annotate_frame(frame, detections, zpx, frame_number, count, label):
    """Draw detection boxes, the zone outline, and a count/label overlay on a copy of the frame."""
    out = frame.copy()

    for x1, y1, x2, y2, cx, cy, cls_id, conf in detections:
        in_zone = is_in_zone(cx, cy, zpx)
        color = (0, 255, 0) if in_zone else (0, 0, 255)
        status = "COUNTED" if in_zone else "NOT IN ZONE"
        text = f"{status} {VEHICLE_CLASSES[cls_id]} {conf:.2f}"

        cv2.rectangle(out, (x1, y1), (x2, y2), color, 2)
        cv2.circle(out, (cx, cy), 5, (255, 0, 0), -1)
        cv2.putText(out, text, (x1, max(y1 - 10, 25)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

    cv2.rectangle(out, (zpx["vert_left"], zpx["vert_top"]),
                  (zpx["vert_right"], zpx["vert_bottom"]), (0, 255, 255), 3)
    cv2.rectangle(out, (zpx["hor_left"], zpx["hor_top"]),
                  (zpx["hor_right"], zpx["hor_bottom"]), (0, 255, 255), 3)

    cv2.putText(out, f"{label} | Frame: {frame_number} | Count: {count}",
                (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
    return out


def timecode_to_seconds(timecode):
    """
    Convert "M:SS:MMM" (or "MM:SS:MMM") into seconds.

    Examples:
        "2:08:082" -> 128.082 seconds
        "0:05:500" -> 5.500 seconds
    """
    if isinstance(timecode, (int, float)):
        return float(timecode)

    match = re.fullmatch(r"(\d+):(\d{1,2}):(\d{1,3})", str(timecode).strip())
    if not match:
        raise ValueError(
            f"Invalid timestamp {timecode!r}. Use M:SS:MMM, e.g. 2:08:082."
        )

    minutes, seconds, milliseconds = map(int, match.groups())

    if seconds >= 60:
        raise ValueError(f"Invalid timestamp {timecode!r}: seconds must be 0-59.")
    if milliseconds >= 1000:
        raise ValueError(
            f"Invalid timestamp {timecode!r}: milliseconds must be 0-999."
        )

    return minutes * 60 + seconds + milliseconds / 1000.0


def timecode_to_frame(timecode, fps):
    """Convert a timestamp to the nearest video frame number."""
    return round(timecode_to_seconds(timecode) * fps)


def frame_to_timecode(frame_number, fps):
    """Convert a frame number back to "M:SS:MMM" for display."""
    total_ms = round(frame_number * 1000 / fps)
    minutes, remainder = divmod(total_ms, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{minutes}:{seconds:02d}:{milliseconds:03d}"


def build_windows(fps, intersections, zone_frac):
    """
    Flatten one video's list of intersections into a flat list of
    frame-numbered "windows" -- one per (intersection, phase) pair that
    actually has a timeframe defined.
    """
    windows = []
    for intersection in intersections:
        for phase in ("pre", "true"):
            tf = intersection.get(phase)
            if tf is None:
                # No timeframe defined for this phase (e.g. no "pre" data) -- skip it.
                continue
            start_frame = timecode_to_frame(tf["start"], fps)
            end_frame = timecode_to_frame(tf["end"], fps)

            if end_frame < start_frame:
                raise ValueError(
                    f"{intersection['name']}/{phase}: end timestamp must be "
                    f"at or after start timestamp."
                )

            windows.append({
                "name": intersection["name"],
                "phase": phase,
                "zone_frac": zone_frac,
                "start": start_frame,
                "end": end_frame,
                "start_time": tf["start"],
                "end_time": tf["end"],
                "counts": [],          # list of (frame_number, count)
                "max_count": -1,
                "max_frame_number": None,
                "max_frame_image": None,
            })
    return windows


# ---------------------------------------------------------------------------
# PROCESS ONE VIDEO
# ---------------------------------------------------------------------------
def process_video(video_key, video_path, intersections, zone_frac, model, video_output_dir):
    """
    Run detection on a single video for all of its configured intersections.

    Does two passes over the video:
      1. Read every frame once (only within the frames any window needs),
         run detection, and track the running max count per window.
      2. Re-seek to each window's median-count frame to save an annotated
         image for it too (this needs a second pass since the median can't
         be known until all frames have been counted).

    Writes annotated JPGs, a per-video summary CSV, and a completion marker
    into video_output_dir. Returns the list of summary rows for this video.
    """
    video_output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    if not fps or fps <= 0:
        cap.release()
        raise ValueError(f"Could not determine video FPS for {video_path}.")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    windows = build_windows(fps, intersections, zone_frac)
    if not windows:
        cap.release()
        print(f"[{video_key}] No usable intersections configured -- skipping.")
        return []

    global_start = min(w["start"] for w in windows)
    global_end = min(max(w["end"] for w in windows), total_frames - 1)

    print(f"\n[{video_key}] Video FPS: {fps:.3f} | Total frames: {total_frames}")
    print(f"[{video_key}] Processing frames {global_start}..{global_end}")

    # ---- Pass 1: read every relevant frame, run detection, track max counts ----
    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_number < global_start:
            frame_number += 1
            continue
        if frame_number > global_end:
            break

        active_windows = [w for w in windows if w["start"] <= frame_number <= w["end"]]

        if active_windows:
            height, width = frame.shape[:2]

            results = model.predict(
                frame,
                classes=list(VEHICLE_CLASSES.keys()),
                conf=0.20,
                verbose=False,
            )

            detections = []
            if results[0].boxes is not None:
                boxes = results[0].boxes
                for box, cls_id, conf in zip(
                    boxes.xyxy.cpu().numpy(),
                    boxes.cls.cpu().numpy(),
                    boxes.conf.cpu().numpy(),
                ):
                    cls_id = int(cls_id)
                    x1, y1, x2, y2 = map(int, box)
                    cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
                    detections.append((x1, y1, x2, y2, cx, cy, cls_id, conf))

            for w in active_windows:
                zpx = zone_to_pixels(w["zone_frac"], width, height)
                count = sum(1 for d in detections if is_in_zone(d[4], d[5], zpx))
                w["counts"].append((frame_number, count))

                if VERBOSE_PER_DETECTION:
                    print(f"[{video_key}/{w['name']}/{w['phase']}] frame {frame_number}: {count} in zone")

                if count > w["max_count"]:
                    w["max_count"] = count
                    w["max_frame_number"] = frame_number
                    label = f"{w['name']} ({w['phase']})"
                    w["max_frame_image"] = annotate_frame(
                        frame, detections, zpx, frame_number, count, label
                    )

        frame_number += 1
        if frame_number % 200 == 0:
            print(f"[{video_key}] ...at frame {frame_number}")

    cap.release()

    # ---- Pass 2: re-seek to each window's median-count frame and annotate it ----
    cap = cv2.VideoCapture(video_path)

    summary_rows = []

    for w in windows:
        if not w["counts"]:
            print(f"[{video_key}/{w['name']}/{w['phase']}] No frames processed (check start/end range).")
            continue

        counts_only = [c for _, c in w["counts"]]
        median_count = statistics.median(counts_only)

        # Find the actual frame whose count is closest to the median.
        closest_frame_number, closest_count = min(
            w["counts"], key=lambda fc: abs(fc[1] - median_count)
        )

        cap.set(cv2.CAP_PROP_POS_FRAMES, closest_frame_number)
        ret, frame = cap.read()
        median_image_path = None
        if ret:
            height, width = frame.shape[:2]
            zpx = zone_to_pixels(w["zone_frac"], width, height)

            results = model.predict(
                frame, classes=list(VEHICLE_CLASSES.keys()), conf=0.20, verbose=False
            )
            detections = []
            if results[0].boxes is not None:
                boxes = results[0].boxes
                for box, cls_id, conf in zip(
                    boxes.xyxy.cpu().numpy(),
                    boxes.cls.cpu().numpy(),
                    boxes.conf.cpu().numpy(),
                ):
                    cls_id = int(cls_id)
                    x1, y1, x2, y2 = map(int, box)
                    cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
                    detections.append((x1, y1, x2, y2, cx, cy, cls_id, conf))

            label = f"{w['name']} ({w['phase']}) - MEDIAN"
            median_frame_image = annotate_frame(
                frame, detections, zpx, closest_frame_number, closest_count, label
            )
            median_image_path = video_output_dir / f"{w['name']}_{w['phase']}_median_frame_{closest_frame_number}.jpg"
            cv2.imwrite(str(median_image_path), median_frame_image)

        max_image_path = None
        if w["max_frame_image"] is not None:
            max_image_path = video_output_dir / f"{w['name']}_{w['phase']}_max_frame_{w['max_frame_number']}.jpg"
            cv2.imwrite(str(max_image_path), w["max_frame_image"])

        print(
            f"\n=== [{video_key}] {w['name']} / {w['phase']} "
            f"({w['start_time']} - {w['end_time']}) ==="
        )
        print(f"  Frames processed : {len(w['counts'])}")
        print(
            f"  Max count        : {w['max_count']} at "
            f"{frame_to_timecode(w['max_frame_number'], fps)} "
            f"(frame {w['max_frame_number']})"
            + (f" -> {max_image_path}" if max_image_path else "")
        )
        print(
            f"  Median count     : {median_count} "
            f"(closest actual frame {frame_to_timecode(closest_frame_number, fps)}, "
            f"frame {closest_frame_number}, count {closest_count})"
            + (f" -> {median_image_path}" if median_image_path else "")
        )

        summary_rows.append({
            "video": video_key,
            "intersection": w["name"],
            "phase": w["phase"],
            "frames_processed": len(w["counts"]),
            "max_count": w["max_count"],
            "max_frame": w["max_frame_number"],
            "median_count": median_count,
            "median_frame": closest_frame_number,
        })

    cap.release()

    # Write this video's own summary CSV and a completion marker so a rerun
    # can recognize this video as already done and skip it.
    with open(video_output_dir / "video_summary.csv", "w") as f:
        f.write("video,intersection,phase,frames_processed,max_count,max_frame,median_count,median_frame\n")
        for r in summary_rows:
            f.write(
                f"{r['video']},{r['intersection']},{r['phase']},{r['frames_processed']},"
                f"{r['max_count']},{r['max_frame']},{r['median_count']},{r['median_frame']}\n"
            )
    (video_output_dir / "_DONE.marker").touch()

    return summary_rows


# ---------------------------------------------------------------------------
# MAIN: loop over every video that has a video_path filled in
# ---------------------------------------------------------------------------
def main():
    model = YOLO("yolo11s.pt")

    all_summary_rows = []
    skipped = []

    for video_key, cfg in VIDEOS.items():
        video_path = cfg.get("video_path", "").strip()
        if not video_path:
            skipped.append(video_key)
            continue

        video_output_dir = OUTPUT_DIR / video_key
        marker = video_output_dir / "_DONE.marker"

        if RESUME_MODE and marker.exists():
            print(f"[{video_key}] Already completed in a previous run -- skipping.")
            saved_csv = video_output_dir / "video_summary.csv"
            if saved_csv.exists():
                with open(saved_csv) as f:
                    next(f)  # header
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 8:
                            all_summary_rows.append({
                                "video": parts[0], "intersection": parts[1], "phase": parts[2],
                                "frames_processed": parts[3], "max_count": parts[4],
                                "max_frame": parts[5], "median_count": parts[6], "median_frame": parts[7],
                            })
            continue

        try:
            rows = process_video(
                video_key=video_key,
                video_path=video_path,
                intersections=cfg["intersections"],
                zone_frac=cfg["zone"],
                model=model,
                video_output_dir=video_output_dir,
            )
            all_summary_rows.extend(rows)
        except Exception as e:
            print(f"\n[{video_key}] ERROR: {e} -- skipping this video and continuing.")
            skipped.append(f"{video_key} (error: {e})")

    if skipped:
        print(f"\nSkipped {len(skipped)} video(s) with no video_path set:")
        for k in skipped:
            print(f"  - {k}")

    summary_path = OUTPUT_DIR / "summary.csv"
    with open(summary_path, "w") as f:
        f.write("video,intersection,phase,frames_processed,max_count,max_frame,median_count,median_frame\n")
        for r in all_summary_rows:
            f.write(
                f"{r['video']},{r['intersection']},{r['phase']},{r['frames_processed']},"
                f"{r['max_count']},{r['max_frame']},{r['median_count']},{r['median_frame']}\n"
            )

    print(f"\nDone. Combined summary CSV written to: {summary_path}")
    print(f"All annotated frame images written to: {OUTPUT_DIR}/<video_key>/")


if __name__ == "__main__":
    main()
