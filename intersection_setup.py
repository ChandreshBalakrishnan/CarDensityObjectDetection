"""
Full production configuration for the intersection vehicle-counting pipeline.

This file contains every video (one entry per participant/route combination)
along with its detection zone and the list of intersections (turns) to be
analyzed within that video, including the "pre" and "true" timeframes for
each turn.

This is the actual dataset used for the study -- see vehicle_counter.py for
the engine that consumes this configuration, and README.md for full usage
instructions.

Known data notes:
  - A handful of rows from the original timestamp sheet had no usable data
    or contained timestamp errors and were excluded entirely. See
    all_intersections_reference.csv for the full audit trail of every row,
    including which were excluded and why.
  - P1002_BII_T5B's timing falls outside of the detection zone in the source
    footage; this is a known limitation of the source video, not a script
    bug, and has been accepted as-is.
"""

VIDEOS = {
    "P1001_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1001/P1001_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1001_A_T2A",
                "pre":  {"start": "2:08:085", "end": "2:18:082"},
                "true": {"start": "2:18:082", "end": "2:21:608"},
            },
            {
                "name": "P1001_A_T4ARight",
                "pre":  None,
                "true": {"start": "11:23:695", "end": "11:49:760"},
            },
            {
                "name": "P1001_A_T7",
                "pre":  {"start": "12:32:254", "end": "12:42:265"},
                "true": {"start": "12:42:265", "end": "12:47:881"},
            },
            {
                "name": "P1001_A_T4BRight",
                "pre":  {"start": "15:27:888", "end": "15:37:899"},
                "true": {"start": "15:37:899", "end": "15:41:559"},
            },
        ],
    },
    "P1001_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1001/P1001_2. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1001_B_T2B",
                "pre":  {"start": "1:05:773", "end": "1:15:767"},
                "true": {"start": "1:15:767", "end": "1:18:652"},
            },
            {
                "name": "P1001_B_T4ALeft",
                "pre":  None,
                "true": {"start": "3:46:984", "end": "4:04:580"},
            },
            {
                "name": "P1001_B_T6",
                "pre":  {"start": "4:26:525", "end": "4:36:529"},
                "true": {"start": "4:36:529", "end": "4:40:127"},
            },
            {
                "name": "P1001_B_T4BLeft",
                "pre":  None,
                "true": {"start": "8:55:313", "end": "9:36:693"},
            },
            {
                "name": "P1001_B_T8",
                "pre":  {"start": "18:33:280", "end": "18:43:284"},
                "true": {"start": "18:43:284", "end": "18:45:488"},
            },
        ],
    },
    "P1002_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1002/P1002_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1002_A_T2A",
                "pre":  None,
                "true": {"start": "3:18:854", "end": "3:25:557"},
            },
            {
                "name": "P1002_A_T4ARight",
                "pre":  {"start": "13:23:683", "end": "13:33:683"},
                "true": {"start": "13:33:683", "end": "13:45:332"},
            },
            {
                "name": "P1002_A_T7",
                "pre":  None,
                "true": {"start": "14:42:936", "end": "15:00:101"},
            },
            {
                "name": "P1002_A_T4BRight",
                "pre":  None,
                "true": {"start": "18:35:285", "end": "19:00:243"},
            },
            {
                "name": "P1002_A_T5A",
                "pre":  {"start": "33:36:325", "end": "33:46:325"},
                "true": {"start": "33:46:325", "end": "33:49:364"},
            },
        ],
    },
    "P1002_BI": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1002/P1002_3. Route B I_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1002_BI_T2B",
                "pre":  {"start": "4:12:836", "end": "4:22:839"},
                "true": {"start": "4:22:839", "end": "4:25:344"},
            },
            {
                "name": "P1002_BI_T4ALeft",
                "pre":  None,
                "true": {"start": "8:16:102", "end": "9:13:769"},
            },
            {
                "name": "P1002_BI_T6",
                "pre":  {"start": "9:40:374", "end": "9:50:380"},
                "true": {"start": "9:50:380", "end": "9:54:597"},
            },
            {
                "name": "P1002_BI_T4BLeft",
                "pre":  None,
                "true": {"start": "13:10:447", "end": "13:48:404"},
            },
            {
                "name": "P1002_BI_T3A",
                "pre":  {"start": "19:52:084", "end": "20:02:087"},
                "true": {"start": "20:02:087", "end": "20:07:365"},
            },
            {
                "name": "P1002_BI_T3B",
                "pre":  None,
                "true": {"start": "22:57:010", "end": "23:38:829"},
            },
        ],
    },
    "P1002_BII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1002/P1002_4. Route B II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1002_BII_T5B",
                "pre":  {"start": "6:23:937", "end": "6:33:944"},
                "true": {"start": "6:33:944", "end": "6:37:688"},
            },
        ],
    },
    "P1003_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1003/P1003_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1003_A_T2A",
                "pre":  {"start": "2:30:742", "end": "2:40:750"},
                "true": {"start": "2:40:750", "end": "2:44:819"},
            },
            {
                "name": "P1003_A_T1B",
                "pre":  {"start": "7:30:289", "end": "7:40:293"},
                "true": {"start": "7:40:293", "end": "7:46:207"},
            },
            {
                "name": "P1003_A_T4ARight",
                "pre":  {"start": "12:34:815", "end": "12:44:819"},
                "true": {"start": "12:44:819", "end": "12:48:948"},
            },
            {
                "name": "P1003_A_T7",
                "pre":  {"start": "13:32:710", "end": "13:42:704"},
                "true": {"start": "13:42:704", "end": "13:49:528"},
            },
            {
                "name": "P1003_A_T4BRight",
                "pre":  None,
                "true": {"start": "16:47:249", "end": "17:03:008"},
            },
            {
                "name": "P1003_A_T3A",
                "pre":  None,
                "true": {"start": "24:05:217", "end": "24:59:425"},
            },
            {
                "name": "P1003_A_T5A",
                "pre":  {"start": "29:14:012", "end": "29:24:014"},
                "true": {"start": "29:24:014", "end": "29:26:290"},
            },
        ],
    },
    "P1003_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1003/P1003_2. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1003_B_T2B",
                "pre":  {"start": "1:34:135", "end": "1:44:130"},
                "true": {"start": "1:44:130", "end": "1:48:091"},
            },
            {
                "name": "P1003_B_T4ALeft",
                "pre":  None,
                "true": {"start": "4:42:878", "end": "4:58:133"},
            },
            {
                "name": "P1003_B_T6",
                "pre":  {"start": "5:22:560", "end": "5:32:555"},
                "true": {"start": "5:32:555", "end": "5:41:506"},
            },
            {
                "name": "P1003_B_T4BLeft",
                "pre":  {"start": "9:12:541", "end": "9:22:538"},
                "true": {"start": "9:22:538", "end": "9:30:636"},
            },
            {
                "name": "P1003_B_T1A",
                "pre":  None,
                "true": {"start": "14:56:718", "end": "17:07:346"},
            },
            {
                "name": "P1003_B_T3B",
                "pre":  {"start": "21:30:413", "end": "21:40:409"},
                "true": {"start": "21:40:409", "end": "21:44:791"},
            },
            {
                "name": "P1003_B_T8",
                "pre":  {"start": "24:03:425", "end": "24:13:429"},
                "true": {"start": "24:13:429", "end": "24:15:359"},
            },
            {
                "name": "P1003_B_T5B",
                "pre":  {"start": "19:50:031", "end": "30:00:027"},
                "true": {"start": "30:00:027", "end": "30:02:715"},
            },
        ],
    },
    "P1005_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1005/P1005_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1005_A_T4ARight",
                "pre":  {"start": "12:36:607", "end": "12:46:615"},
                "true": {"start": "12:46:615", "end": "12:50:430"},
            },
            {
                "name": "P1005_A_T4BRight",
                "pre":  {"start": "17:03:167", "end": "17:13:170"},
                "true": {"start": "17:13:170", "end": "17:15:997"},
            },
            {
                "name": "P1005_A_T5A",
                "pre":  {"start": "30:16:197", "end": "30:26:205"},
                "true": {"start": "30:26:205", "end": "30:28:640"},
            },
        ],
    },
    "P1005_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1005/P1005_3. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1005_B_T4ALeft",
                "pre":  None,
                "true": {"start": "4:11:007", "end": "5:29:976"},
            },
            {
                "name": "P1005_B_T6",
                "pre":  None,
                "true": {"start": "6:05:595", "end": "6:29:507"},
            },
            {
                "name": "P1005_B_T4BLeft",
                "pre":  None,
                "true": {"start": "9:26:072", "end": "10:26:722"},
            },
            {
                "name": "P1005_B_T3B",
                "pre":  None,
                "true": {"start": "20:27:955", "end": "20:55:577"},
            },
            {
                "name": "P1005_B_T8",
                "pre":  {"start": "23:28:204", "end": "23:38:209"},
                "true": {"start": "23:38:209", "end": "23:39:575"},
            },
            {
                "name": "P1005_B_T5B",
                "pre":  {"start": "29:06:709", "end": "29:16:781"},
                "true": {"start": "29:16:781", "end": "29:19:241"},
            },
        ],
    },
    "P1006_AI": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1006/P1006_1. Route A I_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1006_AI_T4ARight",
                "pre":  {"start": "11:02:669", "end": "11:12:677"},
                "true": {"start": "11:12:677", "end": "11:22:435"},
            },
        ],
    },
    "P1006_AII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1006/P1006_2. Route A II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1006_AII_T4BRight",
                "pre":  {"start": "1:36:273", "end": "1:46:246"},
                "true": {"start": "1:46:246", "end": "1:53:947"},
            },
        ],
    },
    "P1007_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1007/P1007_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1007_A_T2A",
                "pre":  None,
                "true": {"start": "1:48:845", "end": "1:56:563"},
            },
            {
                "name": "P1007_A_T1B",
                "pre":  {"start": "6:04:845", "end": "6:14:841"},
                "true": {"start": "6:14:841", "end": "6:22:661"},
            },
            {
                "name": "P1007_A_T4ARight",
                "pre":  {"start": "11:34:321", "end": "11:44:321"},
                "true": {"start": "11:44:321", "end": "11:53:161"},
            },
            {
                "name": "P1007_A_T7",
                "pre":  None,
                "true": {"start": "12:51:070", "end": "13:10:008"},
            },
            {
                "name": "P1007_A_T4BRight",
                "pre":  {"start": "16:28:711", "end": "16:38:716"},
                "true": {"start": "16:38:716", "end": "16:42:235"},
            },
        ],
    },
    "P1007_BI": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1007/P1007_2. Route B I_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1007_BI_T2B",
                "pre":  {"start": "1:29:125", "end": "1:39:115"},
                "true": {"start": "1:39:115", "end": "1:44:453"},
            },
            {
                "name": "P1007_BI_T4ALeft",
                "pre":  {"start": "4:23:166", "end": "4:33:177"},
                "true": {"start": "4:33:177", "end": "4:38:872"},
            },
            {
                "name": "P1007_BI_T6",
                "pre":  {"start": "5:04:400", "end": "5:14:403"},
                "true": {"start": "5:14:403", "end": "5:19:911"},
            },
            {
                "name": "P1007_BI_T4BLeft",
                "pre":  None,
                "true": {"start": "8:15:331", "end": "8:55:213"},
            },
            {
                "name": "P1007_BI_T1A",
                "pre":  None,
                "true": {"start": "14:50:503", "end": "15:21:444"},
            },
        ],
    },
    "P1007_BII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1007/P1007_3. Route B II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1007_BII_T8",
                "pre":  {"start": "1:24:531", "end": "1:34:525"},
                "true": {"start": "1:34:525", "end": "1:38:358"},
            },
        ],
    },
    "P1008_AI": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1008/P1008_3. Route A I_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1008_AI_T4ARight",
                "pre":  None,
                "true": {"start": "11:01:761", "end": "11:17:508"},
            },
            {
                "name": "P1008_AI_T7",
                "pre":  {"start": "12:24:713", "end": "12:34:713"},
                "true": {"start": "12:34:713", "end": "12:44:309"},
            },
            {
                "name": "P1008_AI_T4BRight",
                "pre":  {"start": "16:03:849", "end": "16:13:894"},
                "true": {"start": "16:13:894", "end": "16:20:105"},
            },
        ],
    },
    "P1008_AII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1008/P1008_4. Route A II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1008_AII_T5A",
                "pre":  {"start": "2:51:591", "end": "3:01:577"},
                "true": {"start": "3:01:577", "end": "3:04:071"},
            },
        ],
    },
    "P1008_BII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1008/P1008_6. Route B II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1008_BII_T3A",
                "pre":  None,
                "true": {"start": "1:43:687", "end": "2:01:252"},
            },
            {
                "name": "P1008_BII_T3B",
                "pre":  {"start": "3:50:607", "end": "4:00:607"},
                "true": {"start": "4:00:607", "end": "4:05:103"},
            },
            {
                "name": "P1008_BII_T8",
                "pre":  {"start": "6:54:124", "end": "7:04:130"},
                "true": {"start": "7:04:130", "end": "7:07:003"},
            },
            {
                "name": "P1008_BII_T5B",
                "pre":  {"start": "12:42:144", "end": "12:52:144"},
                "true": {"start": "12:52:144", "end": "12:55:800"},
            },
        ],
    },
    "P1009_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1009/P1009_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1009_A_T2A",
                "pre":  {"start": "1:29:333", "end": "1:34:339"},
                "true": {"start": "1:34:339", "end": "1:44:828"},
            },
            {
                "name": "P1009_A_T1B",
                "pre":  {"start": "5:04:181", "end": "5:14:181"},
                "true": {"start": "5:14:181", "end": "5:19:645"},
            },
            {
                "name": "P1009_A_T4ARight",
                "pre":  None,
                "true": {"start": "9:29:649", "end": "9:45:849"},
            },
            {
                "name": "P1009_A_T7",
                "pre":  None,
                "true": {"start": "10:37:793", "end": "10:50:850"},
            },
            {
                "name": "P1009_A_T4BRight",
                "pre":  {"start": "13:24:674", "end": "13:34:667"},
                "true": {"start": "13:34:667", "end": "13:37:323"},
            },
            {
                "name": "P1009_A_T3A",
                "pre":  {"start": "20:55:376", "end": "21:05:377"},
                "true": {"start": "21:05:377", "end": "21:10:655"},
            },
            {
                "name": "P1009_A_T5A",
                "pre":  {"start": "27:25:832", "end": "27:35:832"},
                "true": {"start": "27:35:832", "end": "27:39:597"},
            },
        ],
    },
    "P1009_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1009/P1009_2. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1009_B_T2B",
                "pre":  {"start": "1:10:125", "end": "1:20:134"},
                "true": {"start": "1:20:134", "end": "1:22:976"},
            },
            {
                "name": "P1009_B_T4ALeft",
                "pre":  None,
                "true": {"start": "4:56:017", "end": "5:28:822"},
            },
            {
                "name": "P1009_B_T6",
                "pre":  {"start": "5:49:785", "end": "5:59:789"},
                "true": {"start": "5:59:789", "end": "6:04:294"},
            },
            {
                "name": "P1009_B_T4BLeft",
                "pre":  None,
                "true": {"start": "8:49:482", "end": "9:31:316"},
            },
            {
                "name": "P1009_B_T1A",
                "pre":  None,
                "true": {"start": "16:13:124", "end": "17:39:470"},
            },
            {
                "name": "P1009_B_T3B",
                "pre":  {"start": "20:20:520", "end": "20:30:708"},
                "true": {"start": "20:30:708", "end": "20:37:538"},
            },
            {
                "name": "P1009_B_T8",
                "pre":  {"start": "22:52:245", "end": "23:02:257"},
                "true": {"start": "23:02:257", "end": "23:03:757"},
            },
            {
                "name": "P1009_B_T5B",
                "pre":  {"start": "28:23:880", "end": "28:33:884"},
                "true": {"start": "28:33:884", "end": "28:36:162"},
            },
        ],
    },
    "P1010_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1010/P1010_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1010_A_T2A",
                "pre":  {"start": "1:43:682", "end": "1:53:683"},
                "true": {"start": "1:53:683", "end": "1:59:455"},
            },
            {
                "name": "P1010_A_T4ARight",
                "pre":  {"start": "13:16:375", "end": "13:26:375"},
                "true": {"start": "13:26:375", "end": "13:38:612"},
            },
            {
                "name": "P1010_A_T7",
                "pre":  None,
                "true": {"start": "14:30:449", "end": "14:48:494"},
            },
            {
                "name": "P1010_A_T4BRight",
                "pre":  {"start": "18:38:068", "end": "18:48:086"},
                "true": {"start": "18:48:086", "end": "18:55:289"},
            },
            {
                "name": "P1010_A_T3A",
                "pre":  {"start": "26:34:720", "end": "26:44:721"},
                "true": {"start": "26:44:721", "end": "26:51:487"},
            },
            {
                "name": "P1010_A_T5A",
                "pre":  {"start": "33:29:950", "end": "33:39:956"},
                "true": {"start": "33:39:956", "end": "33:44:025"},
            },
        ],
    },
    "P1010_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1010/P1010_2. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1010_B_T2B",
                "pre":  {"start": "1:49:045", "end": "1:59:048"},
                "true": {"start": "1:59:048", "end": "2:02:180"},
            },
            {
                "name": "P1010_B_T4ALeft",
                "pre":  {"start": "4:50:125", "end": "5:00:128"},
                "true": {"start": "5:00:128", "end": "5:08:651"},
            },
            {
                "name": "P1010_B_T6",
                "pre":  {"start": "5:33:511", "end": "5:43:514"},
                "true": {"start": "5:43:514", "end": "5:47:908"},
            },
            {
                "name": "P1010_B_T4BLeft",
                "pre":  None,
                "true": {"start": "8:39:684", "end": "9:35:110"},
            },
            {
                "name": "P1010_B_T3B",
                "pre":  {"start": "18:12:495", "end": "18:22:498"},
                "true": {"start": "18:22:498", "end": "18:26:717"},
            },
            {
                "name": "P1010_B_T8",
                "pre":  {"start": "21:52:636", "end": "22:02:636"},
                "true": {"start": "22:02:636", "end": "22:04:048"},
            },
            {
                "name": "P1010_B_T5B",
                "pre":  {"start": "28:03:951", "end": "28:13:948"},
                "true": {"start": "28:13:948", "end": "28:16:665"},
            },
        ],
    },
    "P1011_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1011/P1011_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1011_A_T2A",
                "pre":  {"start": "1:29:677", "end": "1:39:676"},
                "true": {"start": "1:39:676", "end": "1:42:516"},
            },
            {
                "name": "P1011_A_T1B",
                "pre":  {"start": "5:34:250", "end": "5:44:247"},
                "true": {"start": "5:44:247", "end": "5:50:669"},
            },
            {
                "name": "P1011_A_T4ARight",
                "pre":  None,
                "true": {"start": "10:44:818", "end": "11:06:440"},
            },
            {
                "name": "P1011_A_T7",
                "pre":  {"start": "11:51:998", "end": "12:01:950"},
                "true": {"start": "12:01:950", "end": "12:06:357"},
            },
            {
                "name": "P1011_A_T4BRight",
                "pre":  {"start": "15:03:334", "end": "15:13:340"},
                "true": {"start": "15:13:340", "end": "15:15:872"},
            },
            {
                "name": "P1011_A_T5A",
                "pre":  {"start": "28:27:087", "end": "28:37:091"},
                "true": {"start": "28:37:091", "end": "28:39:421"},
            },
        ],
    },
    "P1011_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1011/P1011_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1011_B_T2B",
                "pre":  {"start": "1:30:000", "end": "1:40:023"},
                "true": {"start": "1:40:023", "end": "1:45:378"},
            },
            {
                "name": "P1011_B_T4ALeft",
                "pre":  {"start": "3:58:887", "end": "4:08:895"},
                "true": {"start": "4:08:895", "end": "4:14:888"},
            },
            {
                "name": "P1011_B_T6",
                "pre":  {"start": "4:36:592", "end": "4:46:586"},
                "true": {"start": "4:46:586", "end": "4:53:916"},
            },
            {
                "name": "P1011_B_T4BLeft",
                "pre":  {"start": "8:35:186", "end": "8:45:191"},
                "true": {"start": "8:45:191", "end": "8:51:397"},
            },
            {
                "name": "P1011_B_T3A",
                "pre":  {"start": "13:46:646", "end": "14:03:632"},
                "true": {"start": "14:03:632", "end": "14:07:394"},
            },
            {
                "name": "P1011_B_T1A",
                "pre":  {"start": "13:57:390", "end": "14:07:394"},
                "true": {"start": "14:07:394", "end": "14:14:110"},
            },
            {
                "name": "P1011_B_T3B",
                "pre":  {"start": "17:21:530", "end": "17:31:524"},
                "true": {"start": "17:31:524", "end": "17:44:562"},
            },
            {
                "name": "P1011_B_T8",
                "pre":  {"start": "20:14:745", "end": "20:24:740"},
                "true": {"start": "20:24:740", "end": "20:27:519"},
            },
            {
                "name": "P1011_B_T5B",
                "pre":  {"start": "26:02:261", "end": "26:12:266"},
                "true": {"start": "26:12:266", "end": "26:19:277"},
            },
        ],
    },
    "P1012_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1012/P1012_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1012_A_T2A",
                "pre":  None,
                "true": {"start": "1:55:052", "end": "2:07:671"},
            },
            {
                "name": "P1012_A_T1B",
                "pre":  {"start": "6:41:747", "end": "6:51:745"},
                "true": {"start": "6:51:745", "end": "6:58:447"},
            },
            {
                "name": "P1012_A_T4ARight",
                "pre":  {"start": "12:17:955", "end": "12:27:957"},
                "true": {"start": "12:27:957", "end": "12:38:452"},
            },
            {
                "name": "P1012_A_T7",
                "pre":  {"start": "13:21:903", "end": "13:31:914"},
                "true": {"start": "13:31:914", "end": "13:36:780"},
            },
            {
                "name": "P1012_A_T4BRight",
                "pre":  None,
                "true": {"start": "16:42:830", "end": "17:05:690"},
            },
            {
                "name": "P1012_A_T5A",
                "pre":  {"start": "29:28:165", "end": "29:38:172"},
                "true": {"start": "29:38:172", "end": "29:40:824"},
            },
        ],
    },
    "P1012_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1012/P1012_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1012_B_T2B",
                "pre":  {"start": "1:34:166", "end": "1:44:169"},
                "true": {"start": "1:44:169", "end": "1:48:097"},
            },
            {
                "name": "P1012_B_T4ALeft",
                "pre":  {"start": "4:39:894", "end": "4:49:888"},
                "true": {"start": "4:49:888", "end": "4:56:868"},
            },
            {
                "name": "P1012_B_T6",
                "pre":  {"start": "5:22:947", "end": "5:32:948"},
                "true": {"start": "5:32:948", "end": "5:40:563"},
            },
            {
                "name": "P1012_B_T4BLeft",
                "pre":  {"start": "8:53:206", "end": "9:03:201"},
                "true": {"start": "9:03:201", "end": "9:08:213"},
            },
            {
                "name": "P1012_B_T3A",
                "pre":  {"start": "14:32:889", "end": "14:42:899"},
                "true": {"start": "14:42:899", "end": "14:48:225"},
            },
            {
                "name": "P1012_B_T1A",
                "pre":  None,
                "true": {"start": "14:52:552", "end": "15:20:303"},
            },
            {
                "name": "P1012_B_T3B",
                "pre":  {"start": "17:34:185", "end": "17:44:181"},
                "true": {"start": "17:44:181", "end": "17:53:703"},
            },
            {
                "name": "P1012_B_T8",
                "pre":  {"start": "20:12:465", "end": "20:22:468"},
                "true": {"start": "20:22:468", "end": "20:25:326"},
            },
            {
                "name": "P1012_B_T5B",
                "pre":  {"start": "26:32:526", "end": "26:42:529"},
                "true": {"start": "26:42:529", "end": "26:45:888"},
            },
        ],
    },
    "P1013_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1013/P1013_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1013_A_T2A",
                "pre":  {"start": "1:25:932", "end": "1:35:930"},
                "true": {"start": "1:35:930", "end": "1:40:891"},
            },
            {
                "name": "P1013_A_T1B",
                "pre":  {"start": "4:53:000", "end": "5:02:999"},
                "true": {"start": "5:02:999", "end": "5:07:648"},
            },
            {
                "name": "P1013_A_T4ARight",
                "pre":  {"start": "8:57:867", "end": "9:07:872"},
                "true": {"start": "9:07:872", "end": "9:11:421"},
            },
            {
                "name": "P1013_A_T7",
                "pre":  {"start": "9:42:318", "end": "10:02:319"},
                "true": {"start": "10:02:319", "end": "10:11:013"},
            },
            {
                "name": "P1013_A_T4BRight",
                "pre":  {"start": "12:49:838", "end": "12:59:839"},
                "true": {"start": "12:59:839", "end": "13:04:931"},
            },
            {
                "name": "P1013_A_T5A",
                "pre":  {"start": "27:44:448", "end": "27:54:449"},
                "true": {"start": "27:54:449", "end": "27:57:163"},
            },
        ],
    },
    "P1013_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1013/P1013_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1013_B_T2B",
                "pre":  {"start": "1:04:183", "end": "1:14:193"},
                "true": {"start": "1:14:193", "end": "1:20:095"},
            },
            {
                "name": "P1013_B_T4ALeft",
                "pre":  {"start": "4:09:539", "end": "4:19:434"},
                "true": {"start": "4:19:434", "end": "4:26:181"},
            },
            {
                "name": "P1013_B_T6",
                "pre":  {"start": "4:48:019", "end": "4:58:016"},
                "true": {"start": "4:58:016", "end": "5:07:280"},
            },
            {
                "name": "P1013_B_T4BLeft",
                "pre":  {"start": "7:57:657", "end": "8:07:667"},
                "true": {"start": "8:07:667", "end": "8:12:220"},
            },
            {
                "name": "P1013_B_T3A",
                "pre":  None,
                "true": {"start": "13:09:699", "end": "13:53:570"},
            },
            {
                "name": "P1013_B_T1A",
                "pre":  {"start": "13:53:570", "end": "13:59:070"},
                "true": {"start": "13:59:070", "end": "14:07:513"},
            },
            {
                "name": "P1013_B_T3B",
                "pre":  None,
                "true": {"start": "16:34:082", "end": "16:57:866"},
            },
            {
                "name": "P1013_B_T8",
                "pre":  {"start": "19:26:532", "end": "19:36:526"},
                "true": {"start": "19:36:526", "end": "19:39:383"},
            },
            {
                "name": "P1013_B_T5B",
                "pre":  {"start": "25:24:265", "end": "25:34:261"},
                "true": {"start": "25:34:261", "end": "25:37:326"},
            },
        ],
    },
    "P1014_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1014/P1014_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1014_A_T2A",
                "pre":  None,
                "true": {"start": "2:06:779", "end": "2:24:413"},
            },
            {
                "name": "P1014_A_T1B",
                "pre":  {"start": "6:36:818", "end": "6:41:824"},
                "true": {"start": "6:41:824", "end": "6:53:716"},
            },
            {
                "name": "P1014_A_T4ARight",
                "pre":  {"start": "11:54:220", "end": "12:04:219"},
                "true": {"start": "12:04:219", "end": "12:08:234"},
            },
            {
                "name": "P1014_A_T7",
                "pre":  None,
                "true": {"start": "13:41:153", "end": "14:13:465"},
            },
            {
                "name": "P1014_A_T4BRight",
                "pre":  {"start": "17:21:347", "end": "17:26:347"},
                "true": {"start": "17:26:347", "end": "17:36:391"},
            },
            {
                "name": "P1014_A_T5A",
                "pre":  {"start": "28:43:788", "end": "28:53:795"},
                "true": {"start": "28:53:795", "end": "28:56:478"},
            },
        ],
    },
    "P1014_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1014/P1014_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1014_B_T2B",
                "pre":  {"start": "1:30:399", "end": "1:40:390"},
                "true": {"start": "1:40:390", "end": "1:44:908"},
            },
            {
                "name": "P1014_B_T4ALeft",
                "pre":  None,
                "true": {"start": "5:20:608", "end": "5:39:949"},
            },
            {
                "name": "P1014_B_T6",
                "pre":  {"start": "6:05:039", "end": "6:15:041"},
                "true": {"start": "6:15:041", "end": "6:27:105"},
            },
            {
                "name": "P1014_B_T4BLeft",
                "pre":  None,
                "true": {"start": "10:53:056", "end": "11:34:508"},
            },
            {
                "name": "P1014_B_T3A",
                "pre":  None,
                "true": {"start": "16:33:336", "end": "16:49:558"},
            },
            {
                "name": "P1014_B_T1A",
                "pre":  {"start": "16:49:558", "end": "16:55:413"},
                "true": {"start": "16:55:413", "end": "17:02:193"},
            },
            {
                "name": "P1014_B_T3B",
                "pre":  {"start": "19:24:876", "end": "19:34:872"},
                "true": {"start": "19:34:872", "end": "19:39:427"},
            },
            {
                "name": "P1014_B_T8",
                "pre":  {"start": "21:54:754", "end": "22:04:794"},
                "true": {"start": "22:04:794", "end": "22:07:900"},
            },
            {
                "name": "P1014_B_T5B",
                "pre":  {"start": "27:51:625", "end": "28:01:631"},
                "true": {"start": "28:01:631", "end": "28:04:899"},
            },
        ],
    },
    "P1015_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1015/P1015_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1015_A_T2A",
                "pre":  None,
                "true": {"start": "2:08:727", "end": "2:24:068"},
            },
            {
                "name": "P1015_A_T1B",
                "pre":  {"start": "5:58:912", "end": "6:03:917"},
                "true": {"start": "6:03:917", "end": "6:14:783"},
            },
            {
                "name": "P1015_A_T4ARight",
                "pre":  {"start": "11:05:687", "end": "11:15:686"},
                "true": {"start": "11:15:686", "end": "11:22:536"},
            },
            {
                "name": "P1015_A_T7",
                "pre":  {"start": "12:08:770", "end": "12:13:775"},
                "true": {"start": "12:13:775", "end": "12:23:610"},
            },
            {
                "name": "P1015_A_T4BRight",
                "pre":  {"start": "15:08:424", "end": "15:18:434"},
                "true": {"start": "15:18:434", "end": "15:23:430"},
            },
            {
                "name": "P1015_A_T5A",
                "pre":  {"start": "25:41:847", "end": "25:51:857"},
                "true": {"start": "25:51:857", "end": "25:56:886"},
            },
        ],
    },
    "P1015_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1015/P1015_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1015_B_T2B",
                "pre":  None,
                "true": {"start": "1:13:049", "end": "1:35:244"},
            },
            {
                "name": "P1015_B_T4ALeft",
                "pre":  {"start": "4:22:460", "end": "4:32:455"},
                "true": {"start": "4:32:455", "end": "4:39:928"},
            },
            {
                "name": "P1015_B_T6",
                "pre":  None,
                "true": {"start": "5:16:018", "end": "6:03:663"},
            },
            {
                "name": "P1015_B_T4BLeft",
                "pre":  None,
                "true": {"start": "9:58:054", "end": "10:17:039"},
            },
            {
                "name": "P1015_B_T3A",
                "pre":  None,
                "true": {"start": "15:29:011", "end": "16:27:342"},
            },
            {
                "name": "P1015_B_T1A",
                "pre":  {"start": "16:22:342", "end": "16:32:438"},
                "true": {"start": "16:32:438", "end": "16:38:352"},
            },
            {
                "name": "P1015_B_T3B",
                "pre":  {"start": "17:56:396", "end": "18:06:398"},
                "true": {"start": "18:06:398", "end": "19:10:792"},
            },
            {
                "name": "P1015_B_T8",
                "pre":  {"start": "20:29:490", "end": "20:39:495"},
                "true": {"start": "20:39:495", "end": "20:41:928"},
            },
            {
                "name": "P1015_B_T5B",
                "pre":  {"start": "26:08:704", "end": "26:18:709"},
                "true": {"start": "26:18:709", "end": "26:22:130"},
            },
        ],
    },
    "P1016_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1016/P1016_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1016_A_T2A",
                "pre":  {"start": "1:29:365", "end": "1:34:370"},
                "true": {"start": "1:34:370", "end": "1:43:776"},
            },
            {
                "name": "P1016_A_T1B",
                "pre":  {"start": "5:41:278", "end": "5:51:279"},
                "true": {"start": "5:51:279", "end": "5:56:266"},
            },
            {
                "name": "P1016_A_T4ARight",
                "pre":  {"start": "10:37:430", "end": "10:42:440"},
                "true": {"start": "10:42:440", "end": "10:53:827"},
            },
            {
                "name": "P1016_A_T7",
                "pre":  {"start": "11:39:783", "end": "11:49:789"},
                "true": {"start": "11:49:789", "end": "11:54:558"},
            },
            {
                "name": "P1016_A_T4BRight",
                "pre":  {"start": "14:50:171", "end": "15:00:172"},
                "true": {"start": "15:00:172", "end": "15:07:820"},
            },
            {
                "name": "P1016_A_T3A",
                "pre":  {"start": "22:15:198", "end": "22:20:190"},
                "true": {"start": "22:20:190", "end": "22:30:214"},
            },
            {
                "name": "P1016_A_T5A",
                "pre":  {"start": "27:10:011", "end": "27:20:013"},
                "true": {"start": "27:20:013", "end": "27:23:855"},
            },
        ],
    },
    "P1016_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1016/P1016_2. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1016_B_T2B",
                "pre":  {"start": "1:09:116", "end": "1:19:129"},
                "true": {"start": "1:19:129", "end": "1:22:160"},
            },
            {
                "name": "P1016_B_T4ALeft",
                "pre":  {"start": "3:53:333", "end": "4:03:329"},
                "true": {"start": "4:03:329", "end": "4:10:188"},
            },
            {
                "name": "P1016_B_T6",
                "pre":  {"start": "4:53:273", "end": "4:58:271"},
                "true": {"start": "4:58:271", "end": "5:06:422"},
            },
            {
                "name": "P1016_B_T4BLeft",
                "pre":  {"start": "9:32:046", "end": "9:42:059"},
                "true": {"start": "9:42:059", "end": "9:46:141"},
            },
            {
                "name": "P1016_B_T1A",
                "pre":  {"start": "15:17:359", "end": "15:22:364"},
                "true": {"start": "15:22:364", "end": "15:32:864"},
            },
            {
                "name": "P1016_B_T3B",
                "pre":  None,
                "true": {"start": "17:58:889", "end": "18:12:372"},
            },
            {
                "name": "P1016_B_T8",
                "pre":  {"start": "20:46:395", "end": "20:56:391"},
                "true": {"start": "20:56:391", "end": "20:59:009"},
            },
            {
                "name": "P1016_B_T5B",
                "pre":  {"start": "26:38:552", "end": "26:43:550"},
                "true": {"start": "26:43:550", "end": "26:54:668"},
            },
        ],
    },
    "P1017_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1017/P1017_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1017_A_T4ARight",
                "pre":  None,
                "true": {"start": "12:32:133", "end": "12:48:004"},
            },
            {
                "name": "P1017_A_T7",
                "pre":  None,
                "true": {"start": "13:41:110", "end": "14:01:407"},
            },
            {
                "name": "P1017_A_T4BRight",
                "pre":  {"start": "17:47:903", "end": "17:57:919"},
                "true": {"start": "17:57:919", "end": "18:01:088"},
            },
        ],
    },
    "P1018_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1018/P1018_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1018_A_T2A",
                "pre":  {"start": "1:38:219", "end": "1:43:222"},
                "true": {"start": "1:43:222", "end": "1:51:617"},
            },
            {
                "name": "P1018_A_T1B",
                "pre":  {"start": "5:50:949", "end": "5:55:952"},
                "true": {"start": "5:55:952", "end": "6:04:257"},
            },
            {
                "name": "P1018_A_T4ARight",
                "pre":  None,
                "true": {"start": "11:28:087", "end": "11:40:766"},
            },
            {
                "name": "P1018_A_T7",
                "pre":  {"start": "12:23:536", "end": "12:33:542"},
                "true": {"start": "12:33:542", "end": "12:40:532"},
            },
            {
                "name": "P1018_A_T4BRight",
                "pre":  {"start": "15:47:252", "end": "15:57:255"},
                "true": {"start": "15:57:255", "end": "16:00:107"},
            },
            {
                "name": "P1018_A_T5A",
                "pre":  {"start": "30:35:994", "end": "30:45:999"},
                "true": {"start": "30:45:999", "end": "30:53:100"},
            },
        ],
    },
    "P1018_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1018/P1018_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1018_B_T2B",
                "pre":  None,
                "true": {"start": "1:26:474", "end": "1:39:649"},
            },
            {
                "name": "P1018_B_T4ALeft",
                "pre":  None,
                "true": {"start": "4:20:843", "end": "5:05:589"},
            },
            {
                "name": "P1018_B_T6",
                "pre":  {"start": "5:31:294", "end": "5:41:296"},
                "true": {"start": "5:41:296", "end": "5:45:458"},
            },
            {
                "name": "P1018_B_T4BLeft",
                "pre":  None,
                "true": {"start": "10:18:415", "end": "11:38:517"},
            },
            {
                "name": "P1018_B_T3A",
                "pre":  None,
                "true": {"start": "16:45:789", "end": "17:32:553"},
            },
            {
                "name": "P1018_B_T1A",
                "pre":  {"start": "17:32:553", "end": "17:36:925"},
                "true": {"start": "17:36:925", "end": "17:43:764"},
            },
            {
                "name": "P1018_B_T3B",
                "pre":  {"start": "19:02:662", "end": "19:07:663"},
                "true": {"start": "19:07:663", "end": "19:18:779"},
            },
            {
                "name": "P1018_B_T8",
                "pre":  {"start": "21:31:764", "end": "21:41:766"},
                "true": {"start": "21:41:766", "end": "21:44:578"},
            },
            {
                "name": "P1018_B_T5B",
                "pre":  None,
                "true": {"start": "28:02:036", "end": "28:15:427"},
            },
        ],
    },
    "P1019_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1019/P1019_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1019_A_T2A",
                "pre":  None,
                "true": {"start": "1:57:244", "end": "2:10:320"},
            },
            {
                "name": "P1019_A_T1B",
                "pre":  None,
                "true": {"start": "6:05:768", "end": "6:27:001"},
            },
            {
                "name": "P1019_A_T4ARight",
                "pre":  {"start": "10:39:133", "end": "10:44:126"},
                "true": {"start": "10:44:126", "end": "10:55:151"},
            },
            {
                "name": "P1019_A_T7",
                "pre":  None,
                "true": {"start": "12:18:534", "end": "12:32:564"},
            },
            {
                "name": "P1019_A_T4BRight",
                "pre":  {"start": "16:28:597", "end": "16:33:604"},
                "true": {"start": "16:33:604", "end": "16:41:853"},
            },
            {
                "name": "P1019_A_T5A",
                "pre":  {"start": "35:07:481", "end": "35:17:481"},
                "true": {"start": "35:17:481", "end": "35:20:011"},
            },
        ],
    },
    "P1019_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1019/P1019_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1019_B_T2B",
                "pre":  {"start": "1:37:811", "end": "1:47:814"},
                "true": {"start": "1:47:814", "end": "1:51:322"},
            },
            {
                "name": "P1019_B_T4ALeft",
                "pre":  None,
                "true": {"start": "4:59:104", "end": "5:23:886"},
            },
            {
                "name": "P1019_B_T6",
                "pre":  None,
                "true": {"start": "5:58:076", "end": "6:28:324"},
            },
            {
                "name": "P1019_B_T4BLeft",
                "pre":  {"start": "10:24:618", "end": "10:34:621"},
                "true": {"start": "10:34:621", "end": "10:40:282"},
            },
            {
                "name": "P1019_B_T3A",
                "pre":  {"start": "16:00:168", "end": "16:05:179"},
                "true": {"start": "16:05:179", "end": "16:14:002"},
            },
            {
                "name": "P1019_B_T1A",
                "pre":  {"start": "16:12:321", "end": "16:17:331"},
                "true": {"start": "16:17:331", "end": "16:26:734"},
            },
            {
                "name": "P1019_B_T3B",
                "pre":  {"start": "18:30:650", "end": "18:35:660"},
                "true": {"start": "18:35:660", "end": "18:44:055"},
            },
            {
                "name": "P1019_B_T8",
                "pre":  {"start": "20:57:909", "end": "21:07:903"},
                "true": {"start": "21:07:903", "end": "21:10:269"},
            },
            {
                "name": "P1019_B_T5B",
                "pre":  {"start": "26:39:762", "end": "26:49:765"},
                "true": {"start": "26:49:765", "end": "26:55:802"},
            },
        ],
    },
    "P1020_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1020/P1020_1. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1020_A_T2A",
                "pre":  {"start": "1:46:233", "end": "1:56:221"},
                "true": {"start": "1:56:221", "end": "2:03:250"},
            },
            {
                "name": "P1020_A_T1B",
                "pre":  {"start": "6:27:704", "end": "6:32:708"},
                "true": {"start": "6:32:708", "end": "6:41:807"},
            },
            {
                "name": "P1020_A_T4ARight",
                "pre":  {"start": "12:19:092", "end": "12:29:097"},
                "true": {"start": "12:29:097", "end": "12:32:290"},
            },
            {
                "name": "P1020_A_T7",
                "pre":  {"start": "13:13:188", "end": "13:23:186"},
                "true": {"start": "13:23:186", "end": "13:27:360"},
            },
            {
                "name": "P1020_A_T3A",
                "pre":  {"start": "22:55:546", "end": "23:05:544"},
                "true": {"start": "23:05:544", "end": "23:10:279"},
            },
            {
                "name": "P1020_A_T5A",
                "pre":  {"start": "26:51:626", "end": "26:56:630"},
                "true": {"start": "26:56:630", "end": "27:06:048"},
            },
        ],
    },
    "P1020_BI": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1020/P1020_2. Route B I_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1020_BI_T2B",
                "pre":  {"start": "0:52:415", "end": "1:02:407"},
                "true": {"start": "1:02:407", "end": "1:08:848"},
            },
            {
                "name": "P1020_BI_T4ALeft",
                "pre":  {"start": "4:35:374", "end": "4:45:383"},
                "true": {"start": "4:45:383", "end": "4:50:528"},
            },
            {
                "name": "P1020_BI_T6",
                "pre":  None,
                "true": {"start": "5:45:609", "end": "6:21:756"},
            },
        ],
    },
    "P1020_BII": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1020/P1020_3. Route B II_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1020_BII_T4BLeft",
                "pre":  None,
                "true": {"start": "0:58:960", "end": "1:44:802"},
            },
            {
                "name": "P1020_BII_T1A",
                "pre":  {"start": "7:04:681", "end": "7:08:997"},
                "true": {"start": "7:08:997", "end": "7:15:035"},
            },
            {
                "name": "P1020_BII_T3B",
                "pre":  None,
                "true": {"start": "8:55:706", "end": "9:47:614"},
            },
            {
                "name": "P1020_BII_T8",
                "pre":  {"start": "13:04:957", "end": "13:14:960"},
                "true": {"start": "13:14:960", "end": "13:17:550"},
            },
            {
                "name": "P1020_BII_T5B",
                "pre":  {"start": "17:38:628", "end": "17:48:633"},
                "true": {"start": "17:48:633", "end": "17:51:435"},
            },
        ],
    },
    "P1021_A": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1021/P1021_2. Route A_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1021_A_T2A",
                "pre":  None,
                "true": {"start": "1:22:865", "end": "1:52:642"},
            },
            {
                "name": "P1021_A_T1B",
                "pre":  {"start": "6:33:155", "end": "6:43:151"},
                "true": {"start": "6:43:151", "end": "6:48:348"},
            },
            {
                "name": "P1021_A_T4ARight",
                "pre":  {"start": "10:49:860", "end": "10:54:858"},
                "true": {"start": "10:54:858", "end": "11:07:163"},
            },
            {
                "name": "P1021_A_T7",
                "pre":  None,
                "true": {"start": "11:57:524", "end": "12:12:336"},
            },
            {
                "name": "P1021_A_T5A",
                "pre":  {"start": "28:15:440", "end": "28:25:438"},
                "true": {"start": "28:25:438", "end": "28:28:208"},
            },
        ],
    },
    "P1021_B": {
        "video_path": '/Volumes/HFAST3/1_Projects/Guelph_On_Road_Mattea/Data_VideoFiles/P1021/P1021_1. Route B_CAM1.mp4',
        "zone": {
            "vert_left": 0.0, "vert_right": 1.0,
            "hor_top": 0.0, "hor_bottom": 1.0,
        },
        "intersections": [
            {
                "name": "P1021_B_T2B",
                "pre":  {"start": "1:05:994", "end": "1:15:991"},
                "true": {"start": "1:15:991", "end": "1:18:876"},
            },
            {
                "name": "P1021_B_T4ALeft",
                "pre":  {"start": "4:56:563", "end": "5:06:535"},
                "true": {"start": "5:06:535", "end": "5:12:036"},
            },
            {
                "name": "P1021_B_T6",
                "pre":  {"start": "5:34:863", "end": "5:44:860"},
                "true": {"start": "5:44:860", "end": "5:50:400"},
            },
            {
                "name": "P1021_B_T4BLeft",
                "pre":  {"start": "8:20:983", "end": "8:30:980"},
                "true": {"start": "8:30:980", "end": "8:37:861"},
            },
            {
                "name": "P1021_B_T3A",
                "pre":  None,
                "true": {"start": "13:20:304", "end": "14:14:032"},
            },
            {
                "name": "P1021_B_T1A",
                "pre":  {"start": "14:14:032", "end": "14:19:533"},
                "true": {"start": "14:19:533", "end": "14:23:671"},
            },
            {
                "name": "P1021_B_T3B",
                "pre":  None,
                "true": {"start": "15:38:906", "end": "16:10:326"},
            },
            {
                "name": "P1021_B_T8",
                "pre":  {"start": "18:08:670", "end": "18:18:667"},
                "true": {"start": "18:18:667", "end": "18:21:087"},
            },
            {
                "name": "P1021_B_T5B",
                "pre":  {"start": "23:28:011", "end": "23:38:010"},
                "true": {"start": "23:38:010", "end": "23:40:479"},
            },
        ],
    },
}
