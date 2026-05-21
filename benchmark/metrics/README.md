# Evaluation Metrics Implementation

This directory documents the unified metric computation used across all benchmarked methods to ensure fair comparison.

## Metrics

| Metric | Source / Implementation | Reference |
|--------|------------------------|-----------|
| PSNR | `compute_stats.py::compute_psnr()` (MSE-based, dB units) | — |
| SSIM | `skimage.metrics.structural_similarity` | Wang et al., 2004 |
| LPIPS | `lpips.LPIPS(net='vgg')` | Zhang et al., 2018 |

## Usage

All metrics are computed through a single unified script to eliminate implementation bias:

```bash
python ../scripts/compute_stats.py \
    --results_dir ../results/ \
    --output ../results/all_results.csv
```

The script:
1. Loads rendered outputs from each method
2. Computes PSNR, SSIM, and LPIPS against ground-truth images
3. Aggregates results into a single CSV with per-scene and per-method averages

## Metric Details

### PSNR (Peak Signal-to-Noise Ratio)
- **Formula**: `PSNR = 10 · log₁₀(MAX² / MSE)`
- **Range**: [0, ∞) dB, higher is better
- **Typical**: 25-35 dB for novel view synthesis

### SSIM (Structural Similarity Index)
- **Implementation**: `skimage.metrics.structural_similarity(img1, img2, channel_axis=-1, data_range=1.0)`
- **Range**: [0, 1], higher is better
- Captures luminance, contrast, and structure

### LPIPS (Learned Perceptual Image Patch Similarity)
- **Implementation**: `lpips.LPIPS(net='vgg').to(device)`
- **Range**: [0, 1], lower is better
- AlexNet/VGG/SqueezeNet backbones available; VGG used for benchmarking

## Reproducibility Note

Using a **unified metric script** is critical because different codebases may have subtle implementation differences (e.g., data range normalization, color space handling). Our `compute_stats.py` ensures all methods are evaluated identically.
