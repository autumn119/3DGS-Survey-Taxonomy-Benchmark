# 3D Gaussian Splatting: 分类体系与基准评测综述

> **论文配套开源仓库** | [Paper Title / arXiv / DOI TBD]

## 📄 论文概览

- **标题**: 3D Gaussian Splatting: A Comprehensive Taxonomy and Benchmark Survey
- **投稿**: [TBD - e.g., TPAMI / CVPR / NeurIPS]
- **贡献**:
  1. 系统化分类体系：对现有 3DGS 方法按模块、任务、应用场景进行层级分类
  2. 统一基准评测：在一致硬件与数据集条件下复现并对比主流方法的 PSNR/SSIM/LPIPS/FPS/VRAM
  3. 开源工具链：提供可复现的评估脚本与结果分析工具

## 🗂 仓库结构

```
├── README.md               # 本文档
├── LICENSE                 # 开源许可证 (MIT)
├── CITATION.cff            # 引用信息
├── requirements.txt        # Python 依赖
├── resources.md            # 3DGS 方法/代码/数据集/应用场景索引
├── taxonomy/               # 分类体系
│   └── 3dgs_taxonomy.csv   # 方法分类表
├── benchmark/              # 基准评测配置
│   ├── config.md           # 数据集、指标、硬件、软件版本、评测协议
│   ├── datasets/           # 数据集预处理脚本
│   └── metrics/            # 评测指标实现
├── results/                # 评测结果
│   └── all_results.csv     # PSNR / SSIM / LPIPS / FPS / VRAM / 训练时间
├── scripts/                # 分析脚本
│   ├── plot_metrics.py     # 生成论文图表
│   └── compute_stats.py    # 统计汇总
└── figures/                # 图表源文件
    ├── taxonomy_figure.*   # 分类体系图
    ├── timeline.*          # 方法发展时间线
    └── benchmark_charts.*  # 基准评测图表
```

## 🔬 如何复现实验结果

### 1. 环境配置

```bash
# 创建 Conda 环境
conda create -n 3dgs-survey python=3.8
conda activate 3dgs-survey

# 安装依赖
pip install -r requirements.txt
```

### 2. 数据准备

从 `benchmark/datasets/` 目录中的脚本下载并预处理各数据集（Mip-NeRF360, Tanks&Temples, DeepBlending 等）。

### 3. 运行评测

```bash
# 运行统一评测流程
python scripts/run_benchmark.py --method all --output results/
```

### 4. 生成论文图表

```bash
# 生成所有图表
python scripts/plot_metrics.py
```

## 📖 论文引用

```bibtex
@article{yourname20253dgs,
  title={3D Gaussian Splatting: A Comprehensive Taxonomy and Benchmark Survey},
  author={Your Name et al.},
  journal={arXiv preprint},
  year={2025}
}
```

## 📧 联系方式

如有问题，请通过 GitHub Issues 或邮件联系。

---

> 🏷️ 本仓库由论文作者维护，欢迎 Star ⭐ 和贡献！
