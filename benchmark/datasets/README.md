# Dataset Preparation Guide

## Available Datasets

### Mip-NeRF 360

- **Description**: 7 unbounded indoor and outdoor scenes (bicycle, flowers, garden, stump, treehill, room, counter, kitchen, bonsai)
- **Resolution**: 1600×1200 (downscaling factors: 2, 4, 8)
- **Download**: [Mip-NeRF 360 Google Drive](https://jonbarron.info/mipnerf360/)
- **License**: CC-BY 4.0

**Preprocessing:**
```bash
# For 3DGS training at full resolution
python convert.py -s path/to/mipnerf360/scene_name --convert_to_nerfstudio
```

### Tanks & Temples

- **Description**: Large-scale real-world scenes (Truck, Train, M60, Playground, etc.)
- **Resolution**: 1920×1080
- **Download**: [Tanks & Temples Official](https://www.tanksandtemples.org/)
- **License**: Non-commercial research use

**Preprocessing:**
```bash
# COLMAP reconstruction first, then convert
python convert.py -s path/to/tandt/scene_name
```

### DeepBlending

- **Description**: Dr.Johnson (263 images) and Playroom (253 images)
- **Resolution**: 1920×1080
- **Download**: [DeepBlending Official](https://github.com/hfslyc/DeepBlending)
- **License**: Research use

**Preprocessing:**
```bash
python convert.py -s path/to/db/scene_name
```

### Drum Tower (Custom Dataset)

- **Description**: Chinese traditional Dong village drum tower architecture, captured with multi-angle photographs
- **Resolution**: 400×400
- **Train/Val/Test**: 134 / 15 / 56
- **Format**: Blender format (transforms_train.json, transforms_val.json, transforms_test.json)
- **Location**: `/root/autodl-tmp/datasets/drum_tower/`

**Preprocessing:**
```bash
# Dataset already in Blender format
# COLMAP not required — directly loadable by 3DGS pipeline
python train.py -s path/to/drum_tower/zeli  # 752 training images
python train.py -s path/to/drum_tower/chao_li  # 544 training images
```

## Directory Structure Convention

```
datasets/
├── mipnerf360/
│   ├── bicycle/
│   ├── garden/
│   └── ...
├── tandt/
│   ├── train/
│   ├── truck/
│   └── ...
├── db/
│   ├── drjohnson/
│   └── playroom/
└── drum_tower/
    ├── zeli/
    ├── chao_li/
    └── ...
```

## Notes

- For fair comparison, ensure **identical train/test splits** across all methods
- All methods should use the **same COLMAP reconstruction** (if applicable) as the initial point cloud
- Large datasets (Mip-NeRF 360, T&T) may require significant storage (>100 GB)
- The Drum Tower dataset is custom and will be released alongside the paper
