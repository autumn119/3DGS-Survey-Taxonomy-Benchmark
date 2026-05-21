# 3D Gaussian Splatting: A Comprehensive Taxonomy and Benchmark Survey

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20263999.svg)](https://doi.org/10.5281/zenodo.20263999)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Repository for:** *"[Paper Title / arXiv / DOI TBD]"*
> Submitted to: *[TVC / TAMI / CVPR / NeurIPS — TBD]*

This repository provides the complete companion resources for our comprehensive survey and benchmark study of 3D Gaussian Splatting (3DGS) methods. It includes a curated taxonomy, standardized evaluation protocol, benchmark results, automated analysis scripts, and reproducible paper figures.

---

## Repository Structure

```
.
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CITATION.cff                 # Citation metadata (BibTeX-compatible)
├── requirements.txt             # Python / CUDA / PyTorch dependencies
├── resources.md                 # Curated method index, datasets & applications
├── taxonomy/
│   ├── README.md                # Taxonomy documentation
│   └── 3dgs_taxonomy.csv        # Hierarchical method classification table
├── benchmark/
│   ├── config.md                # Datasets, metrics, hardware, evaluation protocol
│   ├── datasets/
│   │   └── README.md            # Dataset preprocessing & preparation guide
│   └── metrics/
│       └── README.md            # Metric implementation details (PSNR/SSIM/LPIPS)
├── scripts/
│   ├── compute_stats.py         # Automated metric computation
│   └── plot_metrics.py          # Figure generation scripts
├── results/
│   └── all_results.csv          # PSNR / SSIM / LPIPS / FPS / VRAM / Training Time
└── figures/
    ├── README.md                # Figure descriptions
    └── taxonomy_reference.png   # Reference taxonomy structure
```

---

## Quick Start

### 1. Clone and install dependencies

```bash
git clone https://github.com/autumn119/3DGS-Survey-Taxonomy-Benchmark.git
cd 3DGS-Survey-Taxonomy-Benchmark
pip install -r requirements.txt
```

### 2. Compute evaluation metrics

```bash
python scripts/compute_stats.py \
    --results_dir path/to/rendered_results/ \
    --output results/all_results.csv
```

This script automatically computes **PSNR**, **SSIM**, and **LPIPS** for all methods against ground-truth images.

### 3. Generate paper figures

```bash
python scripts/plot_metrics.py \
    --csv results/all_results.csv \
    --output_dir figures/
```

---

## Taxonomy Overview

Our taxonomy organizes 3DGS methods along two orthogonal axes:

| Axis | Categories |
|------|-----------|
| **Task / Application** | Optimization, Generalization, Dynamic Scenes, Surface Reconstruction, Editable GS, Physics Simulation, Human Reconstruction, AIGC, Autonomous Driving & SLAM |
| **Technical Module** | Initialization, Attribute Expansion, Splatting, 3D Regularization, 2D Regularization, Pruning, Post-Processing, Integration (PointCloud/Mesh/Triplane) |

The full classification table is available in [`taxonomy/3dgs_taxonomy.csv`](taxonomy/3dgs_taxonomy.csv).

---

## Benchmark Protocol

All methods are evaluated under a **standardized protocol** to ensure fair comparison:

| Item | Specification |
|------|--------------|
| **Datasets** | Mip-NeRF 360, Tanks&Temples, DeepBlending, Custom Drum Tower dataset |
| **Metrics** | PSNR, SSIM, LPIPS (VGG), FPS, GPU VRAM, Training Time |
| **Hardware** | NVIDIA RTX 4090 (24 GB VRAM) |
| **Software** | Ubuntu 22.04, CUDA 11.8, PyTorch 2.x |
| **Reproducibility** | Fixed random seeds, standardized train/test splits, identical resolution |

Full protocol details: [`benchmark/config.md`](benchmark/config.md)

---

## Citation

If you find this repository useful, please cite our paper:

```bibtex
@article{author2025survey,
  title     = {3D Gaussian Splatting: A Comprehensive Taxonomy and Benchmark Survey},
  author    = {[Your Name]},
  journal   = {[Journal/Conference Name]},
  year      = {2025},
  doi       = {10.5281/zenodo.20263999}
}
```

A ready-to-use `CITATION.cff` file is included for GitHub-compatible citation metadata.

---

## License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE) for details.

---

## Acknowledgments

This work builds upon [awesome-3DGS (arXiv:2407.17418)](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) and the [SoTA-Point-Cloud Taxonomy](https://github.com/QingyongHu/SoTA-Point-Cloud). We thank the original 3DGS authors ([Kerbl et al., SIGGRAPH 2023](https://github.com/graphdeco-inria/gaussian-splatting)) for their foundational work.

---

*Last updated: 2026-05-21*
