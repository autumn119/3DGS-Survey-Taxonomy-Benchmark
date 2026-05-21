# 数据集预处理脚本

## 使用方法

将数据集预处理脚本放置在此目录下，例如：

- `download_mipnerf360.py` — 下载并预处理 Mip-NeRF 360
- `download_tnt.py` — 下载并预处理 Tanks & Temples
- `convert_colmap_to_json.py` — COLMAP 到 3DGS 格式转换

## 标准数据集目录结构

```
datasets/
├── mipnerf360/
│   ├── bicycle/
│   │   ├── images/       # 原始图像
│   │   ├── sparse/       # COLMAP 稀疏重建
│   │   └── transforms.json
│   └── ...
├── tanks_and_temples/
│   └── ...
└── drum_tower/           # 本论文自定义鼓楼数据集
    ├── images/
    ├── sparse/
    └── transforms.json
```
