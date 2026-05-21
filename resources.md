# Resources: 3DGS Method Index, Datasets & Applications

> Comprehensive method index built upon [awesome-3DGS (arXiv:2407.17418)](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) and the [SoTA-Point-Cloud Taxonomy (TPAMI 2020)](https://github.com/QingyongHu/SoTA-Point-Cloud).

---

## Table of Contents

1. [Foundational Work](#1-foundational-work)
2. [Optimization — Storage Efficiency](#2-optimization--storage-efficiency)
3. [Optimization — Rendering & Training Efficiency](#3-optimization--rendering--training-efficiency)
4. [Optimization — Photorealism](#4-optimization--photorealism)
5. [Generalization & Sparse Views](#5-generalization--sparse-views)
6. [Dynamic Scene Reconstruction](#6-dynamic-scene-reconstruction)
7. [Surface Reconstruction](#7-surface-reconstruction)
8. [Editable, Relightable & Physics-Aware GS](#8-editable-relightable--physics-aware-gs)
9. [Human Reconstruction](#9-human-reconstruction)
10. [3D Content Generation (AIGC)](#10-3d-content-generation-aigc)
11. [Autonomous Driving & SLAM](#11-autonomous-driving--slam)
12. [Datasets](#12-datasets)
13. [Applications Overview](#13-applications-overview)

---

## 1. Foundational Work

| Method | Venue | Description | Code |
|--------|-------|-------------|------|
| 3D Gaussian Splatting | SIGGRAPH 2023 | Original 3DGS: anisotropic 3D Gaussians + tile-based rasterizer | [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) |
| 3D Gaussian Splatting Survey | arXiv 2024 | Comprehensive survey covering 200+ methods (awesome-3DGS) | [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) |

---

## 2. Optimization — Storage Efficiency

### Improving Efficient Gaussian Representations

| Method | Description | Code |
|--------|-------------|------|
| Scaffold-GS | Anchor points distribute local 3D Gaussians with view-dependent attribute prediction | [city-super/Scaffold-GS](https://github.com/city-super/Scaffold-GS) |
| GES | Generalized Exponential Splatting — fewer particles with identical quality | [abdullahamdi/ges](https://github.com/abdullahamdi/ges) |
| LightGaussian | 15× compression via SH distillation + 200 FPS rendering | [VITA-Group/LightGaussian](https://github.com/VITA-Group/LightGaussian) |
| Compact3D | Vector Quantization (VQ) for compressing 3DGS attributes | [ucdvision/compact3d](https://github.com/ucdvision/compact3d) |
| ContextGS | Anchor-level context model for entropy-based compression | — |
| F-3DGS | Factorized coordinates and representation decomposition | — |

### Pruning & Compression

| Method | Description | Code |
|--------|-------------|------|
| Compressed 3DGS | Sensitivity-aware SH pruning + quantization | [KeKsBoTer/c3dgs](https://github.com/KeKsBoTer/c3dgs) |
| Gaussian-Forest | Hierarchical scene decomposition (forest structure) | — |
| Tangram-Splatting | Tangram-shaped primitives for storage optimization | — |
| EAGLES | Efficient acceleration via Gaussian-level encoding | — |
| Compact 3D Scene via Self-Organizing Gaussian Grids | Grid-based layout for compact storage | — |

---

## 3. Optimization — Rendering & Training Efficiency

| Method | Focus | Description | Code |
|--------|-------|-------------|------|
| DISTWAR | Training | Warp-level high-throughput rasterization for faster training | — |
| I3DGS | Training | Multi-dimensional optimization improvements | — |
| GSCore | Rendering | Custom GPU kernel for hardware-accelerated GS rendering | — |
| RadSplat | Rendering | Radiance field acceleration via splatting + tiny MLP | — |
| StopThePop | Rendering | Sorted-blending optimization to reduce rasterization overhead | — |
| Hierarchical 3D GS | LOD | Level-of-Detail hierarchy for kilometer-scale scenes | — |

---

## 4. Optimization — Photorealism

### Anti-Aliasing & Multi-Scale

| Method | Description | Code |
|--------|-------------|------|
| Mip-Splatting | Mip-map-inspired 3D smoothing filter + 2D Mip filter | [autonomousvision/mip-splatting](https://github.com/autonomousvision/mip-splatting) |
| Multi-Scale 3DGS | Multi-scale Gaussian representation for alias-free rendering | [ZehaoYu/multi_scale_3DGS](https://github.com/ZehaoYu/multi_scale_3DGS) |
| SA-GS | Scale-adaptive 3DGS for training-free anti-aliasing | — |

### View-Dependent Effects

| Method | Description | Code |
|--------|-------------|------|
| GaussianShader | Normal-based shading for reflective/refractive surfaces | [Asparagus15/GaussianShader](https://github.com/Asparagus15/GaussianShader) |
| Spec-Gaussian | Anisotropic spherical Gaussian for specular highlights | — |

### Frequency & Detail Enhancement

| Method | Description | Code |
|--------|-------------|------|
| FreGS | Frequency annealing regularization — progressive detail enhancement | [JiahuiFan/FreGS](https://github.com/JiahuiFan/FreGS) |
| GaussianPro | Progressive propagation with patch-matching optimization | [kcheng1021/GaussianPro](https://github.com/kcheng1021/GaussianPro) |

### Robustness

| Method | Description | Code |
|--------|-------------|------|
| DeblurGS | Handles real-world camera motion blur in 3DGS | [chaphlagical/Deblur-GS](https://github.com/chaphlagical/Deblur-GS) |
| Mirror-3DGS | Accurate mirror reflection rendering | — |
| Relightable 3DGS | BRDF decomposition + ray-traced shadow | [shunsukesaito](https://github.com/shunsukesaito) |
| Touch-GS | Visual-tactile joint supervision for reconstruction | — |

---

## 5. Generalization & Sparse Views

### Generalizable (Few-Shot / Zero-Shot)

| Method | Description | Code |
|--------|-------------|------|
| pixelSplat | 3DGS reconstruction from image pairs via epipolar transformers | [dcharatan/pixelsplat](https://github.com/dcharatan/pixelsplat) |
| MVSplat | Cost-volume-based sparse-view efficient reconstruction | [TomyDeng/MVSplat](https://github.com/TomyDeng/MVSplat) |
| Splatter Image | Lightning-fast single-view GS reconstruction | [szymanowiczs/splatter-image](https://github.com/szymanowiczs/splatter-image) |
| Triplane Meets GS | Transformer-based single-view 3DGS prediction | — |
| AGG | Amortized Generative GS for single-image to 3D | — |
| FreeSplat | Free-viewpoint synthesis for indoor scenes | — |
| GGRt | Pose-free generalizable 3DGS | — |
| latentSplat | Latent-space 3DGS generation | — |
| GPS-Gaussian | Generalizable pixel-wise 3DGS for human reconstruction | — |

### Sparse-View Settings

| Method | Description | Code |
|--------|-------------|------|
| FSGS | Few-Shot (3 views) GS with proximity-guided unpooling | [VITA-Group/FSGS](https://github.com/VITA-Group/FSGS) |
| DNGaussian | Depth-regularized normal GS for sparse-view optimization | [Fictionarry/DNGaussian](https://github.com/Fictionarry/DNGaussian) |
| GaussianObject | High-quality reconstruction from only 4 images | — |
| CoR-GS | Co-regularized GS for consistent sparse-view reconstruction | — |
| SparseGS | Real-time sparse-view 3DGS | — |

### Large-Scene Reconstruction

| Method | Description | Code |
|--------|-------------|------|
| VastGaussian | Partition-based distributed 3DGS for large scenes | — |
| CityGaussian | Real-time high-quality large-scale scene rendering | — |
| Octree-GS | Octree-structured GS for consistent multi-view large scenes | — |
| Hierarchical 3D GS (Kerbl et al.) | LOD hierarchy for very large captures (km-scale) | — |

---

## 6. Dynamic Scene Reconstruction

| Method | Setting | Description | Code |
|--------|---------|-------------|------|
| 4D Gaussian Splatting | Multi-view | 4D Gaussians: multi-resolution HexPlane + lightweight MLP | [fudan-zvg/4d-gaussian-splatting](https://github.com/fudan-zvg/4d-gaussian-splatting) |
| Deformable 3DGS | Monocular | Learnable deformation field + static canonical GS | [ingra14m/Deformable-3D-Gaussians](https://github.com/ingra14m/Deformable-3D-Gaussians) |
| 3DGStream | Multi-view + streaming | Online free-viewpoint video with frame-by-frame transformation | — |
| GauFRe | Monocular | Deformation field for real-time dynamic scene rendering | — |
| SC-GS | Sparse control | Sparse control points for editable dynamic scenes | — |
| DynMF | Neural motion | Neural motion decomposition for dynamic GS | — |
| Gaussian-Flow | 4D | Dual-domain 4D particle reconstruction | — |
| STGS | Spatiotemporal | Spatio-temporal GS with time-conditioned attributes | — |
| SWAGS | Adaptive window | Sliding-window adaptive Gaussian splatting for long videos | — |
| GaGS | Geometry-aware | 3D geometry-aware deformable GS for dynamic view synthesis | — |

---

## 7. Surface Reconstruction

| Method | Description | Code |
|--------|-------------|------|
| SuGaR | Mesh extraction via Poisson reconstruction on GS-aligned surface | [Anttwo/SuGaR](https://github.com/Anttwo/SuGaR) |
| 2D Gaussian Splatting | 2D oriented disks (surfels) instead of 3D ellipsoids | [hbb1/2d-gaussian-splatting](https://github.com/hbb1/2d-gaussian-splatting) |
| Gaussian Surfels | Unbiased depth rendering + normal regularization for high-quality surfaces | [turandai/gaussian_surfels](https://github.com/turandai/gaussian_surfels) |
| GSDF | Gaussian Splatting + Signed Distance Function joint optimization | — |
| 3DGSR | Implicit surface reconstruction from 3DGS via differentiable Poisson solver | — |
| Gaussian Opacity Fields | Compact surface representation using opacity-aligned Gaussians | — |
| Trim 3DGS | Exact geometry refinement for 3DGS | — |
| NeuSG | Neural Implicit Surface-Guided 3DGS | — |
| PGSR | Planar-based GS for enhanced surface reconstruction | — |

---

## 8. Editable, Relightable & Physics-Aware GS

### Editing

| Method | Description | Code |
|--------|-------------|------|
| GaussianEditor | Text-guided 3D scene editing via semantic tracing | [buaacyw/GaussianEditor](https://github.com/buaacyw/GaussianEditor) |
| Gaussian Grouping | Open-world scene segmentation and grouping | — |
| Segment Any 3DGS | SAM-integrated 3DGS segmentation | — |

### Relighting

| Method | Description | Code |
|--------|-------------|------|
| Relightable 3DGS | Physically-based BRDF decomposition + environment lighting | [shunsukesaito](https://github.com/shunsukesaito) |
| GS-IR | Inverse rendering with 3DGS | — |
| PRTGaussian | Precomputed radiance transfer with Gaussians | — |

### Physics

| Method | Description | Code |
|--------|-------------|------|
| PhysGaussian | Physics-integrated GS via continuum mechanics on particles | — |
| Spring-Gaus | Spring-mass energy model for elastic GS | — |

---

## 9. Human Reconstruction

### Body Reconstruction

| Method | Description | Code |
|--------|-------------|------|
| Animatable Gaussians | Animatable body avatars from multi-view video | [animatable-gaussians](https://github.com/animatable-gaussians) |
| GauHuman | Articulated GS from monocular videos (SMPL-guided) | [skhu101/GauHuman](https://github.com/skhu101/GauHuman) |
| 3DGS-Avatar | Deformable 3DGS for animatable body avatars | — |
| HUGS | Holistic body + clothing reconstruction via GS | [machine-perception-robotics-group/HUGS](https://github.com/machine-perception-robotics-group/HUGS) |
| ASH | Animatable surface-based human reconstruction | — |
| GaussianAvatar | Efficient monocular human avatar with 3DGS | — |

### Head Reconstruction

| Method | Description | Code |
|--------|-------------|------|
| GaussianAvatars | Photorealistic head avatars with rigged 3D Gaussians | [ShenhanQian/GaussianAvatars](https://github.com/ShenhanQian/GaussianAvatars) |
| Gaussian Head Avatar | High-fidelity head avatar via dynamic 3DGS | — |
| GaussianTalker | Real-time audio-driven talking head synthesis | — |
| FlashAvatar | Real-time high-fidelity head avatar reconstruction | — |

### Hair & Clothing

| Method | Description | Code |
|--------|-------------|------|
| GaussianHair | Strand-level hair modeling with GS | — |
| Gaussian Shell Maps | Efficient body surface GS with shell maps | — |

---

## 10. 3D Content Generation (AIGC)

### Text-to-3D

| Method | Description | Code |
|--------|-------------|------|
| DreamGaussian | Efficient text-to-3D via 3DGS + mesh refinement | [dreamgaussian/dreamgaussian](https://github.com/dreamgaussian/dreamgaussian) |
| GaussianDreamer | Fast text-to-3D generation with 3DGS bridging 2D and 3D diffusion | — |
| BrightDreamer | Generic text-to-3D generation with faster optimization | — |
| Hyper-3DG | Hypergraph-based text-to-3D GS generation | — |
| GVGEN | Volumetric representation for text-to-3D generation | — |

### Image-to-3D / Multi-View-to-3D

| Method | Description | Code |
|--------|-------------|------|
| LGM | Large Multi-View Gaussian Model for high-resolution 3D content | [3DTopia/LGM](https://github.com/3DTopia/LGM) |
| GS-LRM | Large Reconstruction Model for 3DGS from 4+ input views | — |
| IM-3D | Iterative multi-view diffusion + 3DGS generation | — |
| GRM | Gaussian Reconstruction Model with triplane backbone | — |

### Scene Generation

| Method | Description | Code |
|--------|-------------|------|
| LucidDreamer | Domain-free scene generation via SDS optimization | [EnVision-Research/LucidDreamer](https://github.com/EnVision-Research/LucidDreamer) |
| GALA3D | Layout-guided complex scene generation via GS | — |
| CG3D | Compositional 3D scene generation | — |
| RealmDreamer | Text-to-3D scene generation with 3DGS | — |

### 4D Generation

| Method | Description | Code |
|--------|-------------|------|
| DreamGaussian4D | Generative 4D GS from text/video input | [jiawei-ren/dreamgaussian4d](https://github.com/jiawei-ren/dreamgaussian4d) |
| GaussianFlow | Splatting Gaussian flow for 4D content creation | — |
| 4DGen | Spatio-temporal consistent 4D generation from monocular video | — |
| Align Your Gaussians | Text-to-4D dynamic scene generation | — |

### Diffusion + 3DGS

| Method | Description | Code |
|--------|-------------|------|
| GaussianDiffusion | Diffusion model for 3D Gaussian generation | — |
| HumanGaussian | Text-driven 3D human generation with GS | — |
| ProlificDreamer | Variational Score Distillation for high-fidelity 3D | — |

---

## 11. Autonomous Driving & SLAM

### Driving Scenes

| Method | Description | Code |
|--------|-------------|------|
| Street Gaussians | Explicit dynamic scene modeling for autonomous driving | [zju3dv/street_gaussians](https://github.com/zju3dv/street_gaussians) |
| DrivingGaussian | Composite dynamic Gaussian splatting for surround-view scenarios | — |
| HUGS | Holistic urban 3D scene understanding via GS | — |
| S³Gaussian | Self-supervised street GS for autonomous driving | — |
| GaussianBeV | Birds-eye-view representation enhanced by 3DGS | — |

### SLAM

| Method | Description | Code |
|--------|-------------|------|
| SplaTAM | RGB-D SLAM: GS map + differentiable rendering + silhouette guidance | [spla-tam/SplaTAM](https://github.com/spla-tam/SplaTAM) |
| GS-SLAM | Dense visual SLAM with 3DGS | [Gaussian-SLAM](https://github.com/Gaussian-SLAM) |
| Gaussian-SLAM (Yugay et al.) | Photo-realistic dense SLAM | [VladimirYugay/Gaussian-SLAM](https://github.com/VladimirYugay/Gaussian-SLAM) |
| Photo-SLAM | Real-time localization + photorealistic mapping | — |
| SGS-SLAM | Semantic GS SLAM with scene understanding | — |
| NEDS-SLAM | Neural Explicit Dense Semantic SLAM | — |
| RTG-SLAM | Real-time Gaussian SLAM | — |

### Navigation

| Method | Description | Code |
|--------|-------------|------|
| GaussNav | 3DGS-based visual language navigation | — |
| GS-Planner | Active reconstruction path planning with GS | — |

---

## 12. Datasets

| Dataset | Scenes | Resolution | License | Link |
|---------|--------|-----------|---------|------|
| Mip-NeRF 360 | 9 | 1600×1200 | CC-BY 4.0 | [Download](https://jonbarron.info/mipnerf360/) |
| Tanks & Temples | 14 | 1920×1080 | Research use | [Download](https://www.tanksandtemples.org/) |
| DeepBlending | 2 | 1920×1080 | Research use | [Download](https://github.com/hfslyc/DeepBlending) |
| NeRF Synthetic (Blender) | 8 | 800×800 | CC-BY 4.0 | [Download](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1) |
| Drum Tower (Custom) | 2+ | 400×400 | TBD (with paper) | — |

---

## 13. Applications Overview

| Application Domain | Key Methods | Typical Metrics |
|--------------------|-------------|-----------------|
| Novel View Synthesis | 3DGS, Mip-Splatting, Scaffold-GS | PSNR, SSIM, LPIPS, FPS |
| 3D Content Creation | DreamGaussian, LGM, LucidDreamer | CLIP score, User study, FID |
| Human Avatar | GauHuman, GaussianAvatars | PSNR, SSIM, LPIPS, FID |
| Autonomous Driving | Street Gaussians, DrivingGaussian | PSNR, SSIM, mIoU |
| SLAM | SplaTAM, GS-SLAM | ATE, PSNR, FPS |
| Surface Reconstruction | SuGaR, 2D GS, Gaussian Surfels | Chamfer-L1, F-score, Normal error |

---

*Last updated: 2026-05-21 — based on awesome-3DGS arXiv:2407.17418*
