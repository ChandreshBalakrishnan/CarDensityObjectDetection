# Intersection Vehicle Counter

Counts vehicles (cars, motorcycles, buses, and trucks) in a defined region of traffic footage during specific timeframes, using a YOLO object detector. Built for analyzing vehicle density at intersections across many participant driving videos.

## Features

- Detects and counts vehicles frame-by-frame using [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- Configurable detection zone per video (a region of the frame to count within)
- Supports "pre" and "true" timeframes per turn/intersection, for before/during comparisons
- Reports both the **maximum** vehicle count and the **median** vehicle count for each timeframe, with annotated frame images saved for both
- Processes many videos in a single run, each with its own zone and set of timeframes
- Resumable — if a run is interrupted, already-completed videos are skipped on the next run instead of being reprocessed

## Requirements

```bash
pip install ultralytics opencv-python
```

The first run downloads the YOLO model weights (`yolo11s.pt`) automatically, so an internet connection is needed at least once.

## Project structure

```
.
├── car_density_counter.py   # main script — detection, counting, and reporting logic
└── intersection_setup.py    # configuration — video paths, zones, and timeframes
```

**`car_density_counter.py`** is the engine. It contains all the processing logic and a small example configuration, so you can see the expected format and test the pipeline without any real data. It's meant to be reused across projects — just swap in your own configuration.

**`intersection_setup.py`** is pure configuration, no logic. It defines every video to process, split out from the engine so the data can be edited independently without touching the code.

## Usage

### 1. Try the built-in example

`car_density_counter.py` ships with a small example config (`EXAMPLE_VIDEO_1`). Fill in a real video path and run:

```bash
python3 car_density_counter.py
```

### 2. Use your own configuration

Define your videos in `intersection_setup.py`:

```python
VIDEOS = {
    "MyVideo_1": {
        "video_path": "/path/to/video.mp4",
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "MyVideo_1_TurnA",
                "pre":  {"start": "0:03:333", "end": "0:13:333"},
                "true": {"start": "0:13:333", "end": "0:18:000"},
            },
            {
                "name": "MyVideo_1_TurnB",
                "pre":  None,  # no pre-turn data for this one
                "true": {"start": "1:05:000", "end": "1:20:500"},
            },
        ],
    },
}
```

Then in `car_density_counter.py`, swap the example config for an import:

```python
# VIDEOS = { "EXAMPLE_VIDEO_1": { ... } }
from intersection_setup import VIDEOS
```

Run it:

```bash
python3 car_density_counter.py
```

Every video with a non-empty `video_path` gets processed. Leave `video_path` as `""` to skip a video without deleting its config.

## Configuration reference

| Key | Description |
|---|---|
| `video_path` | Path to the video file. Leave as `""` to skip. |
| `zone` | The detection region, as fractions (`0.0`–`1.0`) of frame width/height. Shaped like a plus sign: a vertical strip (`vert_left`–`vert_right`) spans the full frame height, and a horizontal strip (`hor_top`–`hor_bottom`) spans the full frame width. A detection counts if its center falls in either strip. Set all four to `0.0`/`1.0` to cover the entire frame. |
| `intersections` | List of turns/events to analyze in this video. Each has a `name`, an optional `pre` timeframe, and a required `true` timeframe. |
| Timestamps | Format is `"M:SS:MMM"` (minutes:seconds:milliseconds), e.g. `"2:08:082"` = 2 minutes, 8.082 seconds. |

## Output

Results are written to `intersection_outputs/`:

```
intersection_outputs/
├── summary.csv                                 # combined results across all videos
└── <video_key>/
    ├── video_summary.csv                        # this video's results only
    ├── _DONE.marker                              # marks this video as fully processed
    ├── <turn>_<phase>_max_frame_<n>.jpg          # frame with the highest count
    └── <turn>_<phase>_median_frame_<n>.jpg       # frame closest to the median count
```

`summary.csv` columns: `video, intersection, phase, frames_processed, max_count, max_frame, median_count, median_frame`

## Resuming an interrupted run

If a run gets cut off partway through (e.g. a network drive disconnects), you don't need to start over. Each video that finishes successfully gets a `_DONE.marker` file in its output folder. On the next run, any video with that marker is skipped automatically, and its previous results are pulled back in when building the combined `summary.csv`. Only videos that didn't finish get reprocessed.

This is controlled by two settings near the top of `car_density_counter.py`:

```python
CLEAR_OUTPUT_DIR_EACH_RUN = False  # keep False to resume; True wipes everything
RESUME_MODE = True                 # keep True to skip already-completed videos
```

To force a specific video to be reprocessed (e.g. after fixing its timestamps), delete just that video's marker:

```bash
rm intersection_outputs/<video_key>/_DONE.marker
```

**Tip:** if running over a network-mounted drive on macOS, disable display/system sleep for the duration of the run, or use `caffeinate -i python3 car_density_counter.py` — the machine sleeping will drop the network connection mid-run.

## License

MIT
