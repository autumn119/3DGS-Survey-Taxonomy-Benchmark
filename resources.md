# Resources: 3DGS 方法、代码、数据集与应用场景索引

## 主要 3DGS 方法及开源代码

| 方法 | 年份 | 发表 | 代码仓库 | 特点 |
|------|------|------|----------|------|
| 3D Gaussian Splatting | 2023 | SIGGRAPH | [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) | 原始方法 |
| Mip-Splatting | 2024 | CVPR | [autonomousvision/mip-splatting](https://github.com/autonomousvision/mip-splatting) | 抗锯齿 |
| Scaffold-GS | 2024 | CVPR | [city-super/Scaffold-GS](https://github.com/city-super/Scaffold-GS) | 锚点生长控制 |
| 4D Gaussian Splatting | 2024 | CVPR | [fudan-zvg/4d-gaussian-splatting](https://github.com/fudan-zvg/4d-gaussian-splatting) | 动态场景 |
| SuGaR | 2024 | CVPR | [Anttwo/SuGaR](https://github.com/Anttwo/SuGaR) | 网格提取 |
| Compact3D | 2024 | ECCV | [ucdvision/compact3d](https://github.com/ucdvision/compact3d) | 量化压缩 |
| 2D Gaussian Splatting | 2024 | SIGGRAPH | [hbb1/2d-gaussian-splatting](https://github.com/hbb1/2d-gaussian-splatting) | 2D 基元 |
| GaussianPro | 2024 | TPAMI | [kcheng1021/GaussianPro](https://github.com/kcheng1021/GaussianPro) | 渐进优化 |
| PixelGS | 2024 | ECCV | [zhengzhang01/PixelGS](https://github.com/zhengzhang01/PixelGS) | 像素级稠密化 |
| InstantSplat | 2024 | ECCV | [NVIDIAGameWorks/kaolin-wisp](https://github.com/NVIDIAGameWorks/kaolin-wisp) | 稀疏视图 |

## 常用数据集

| 数据集 | 链接 | 类型 |
|--------|------|------|
| Mip-NeRF 360 | [下载](https://jonbarron.info/mipnerf360/) | 室内外高分辨率 |
| Tanks & Temples | [下载](https://www.tanksandtemples.org/) | 大规模室外 |
| Deep Blending | [下载](https://github.com/facebookresearch/NSVF) | 复杂光照 |
| Synthetic NeRF | [下载](https://www.matthewtancik.com/nerf) | 合成物体 |
| ScanNet++ | [下载](https://kaldir.vc.in.tum.de/scannetpp/) | 室内扫描 |

## 典型任务与应用场景

| 任务 | 描述 | 代表性工作 |
|------|------|------------|
| 新视角合成 (NVS) | 从稀疏图像生成新视角 | 3DGS, Mip-Splatting |
| 表面重建 | 从3DGS提取几何表面 | SuGaR, 2DGS |
| 动态场景重建 | 处理运动物体和时变场景 | 4DGS, Deformable-3DGS |
| 大规模场景 | 城市级/户外大场景重建 | VastGaussian, CityGaussian |
| 稀疏视图重建 | 极少量输入图像 | InstantSplat, pixelSplat |
| 文本到3D | 文本描述生成3D内容 | DreamGaussian, LGM |
| 3D 编辑 | 编辑3DGS场景中的物体 | GaussianEditor, GScream |
| AR/VR | 实时渲染的增强/虚拟现实 | Mobile-GS, LightGaussian |
| 自动驾驶 | 街景重建与仿真 | Street Gaussians, DrivingGaussian |
| SLAM | 同时定位与建图 | SplaTAM, GS-SLAM |
| 传统建筑数字化 | 鼓楼/古建筑高精度重建 | (本论文鼓楼场景) |

## 相关综述与工具

| 资源 | 链接 | 说明 |
|------|------|------|
| Awesome-3DGS | [GitHub](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | 论文列表 |
| Nerfstudio | [GitHub](https://github.com/nerfstudio-project/nerfstudio) | NeRF/3DGS 统一框架 |
| gsplat | [GitHub](https://github.com/nerfstudio-project/gsplat) | 高效3DGS CUDA实现 |
| ThreeStudio | [GitHub](https://github.com/threestudio-project/threestudio) | 3D AIGC 统一框架 |
