# Benchmark Configuration & Evaluation Protocol

## Datasets

| Dataset | Resolution | Train / Val / Test | Description |
|---------|-----------|---------------------|-------------|
| Mip-NeRF 360 | 1600×1200 | scene-dependent | 7 indoor + outdoor unbounded scenes |
| Tanks & Temples | 1920×1080 | scene-dependent | Large-scale real-world scenes |
| DeepBlending | 1920×1080 | scene-dependent | Dr.Johnson / Playroom |
| Drum Tower Custom | 400×400 | 134 / 15 / 56 | Chinese traditional architecture |

## Evaluation Metrics

| Metric | Abbreviation | Implementation | Range | Better |
|--------|-------------|----------------|-------|--------|
| Peak Signal-to-Noise Ratio | PSNR | MSE-based (dB) | [0, ∞) | ↑ Higher |
| Structural Similarity Index | SSIM | `skimage.metrics.structural_similarity` | [0, 1] | ↑ Higher |
| Learned Perceptual Image Patch Similarity | LPIPS | `lpips.LPIPS(net='vgg')` | [0, 1] | ↓ Lower |
| Frames Per Second | FPS | Wall-clock rendering time | [0, ∞) | ↑ Higher |
| GPU VRAM | VRAM | `nvidia-smi` peak memory (GB) | [0, 24] | ↓ Lower |
| Training Time | T (min) | Wall-clock optimization time | [0, ∞) | ↓ Lower |

## Hardware Configuration

| Component | Specification |
|-----------|--------------|
| GPU | NVIDIA RTX 4090 (24 GB GDDR6X) |
| CPU | Intel Xeon Gold 6330 |
| RAM | 120 GB DDR4 |
| OS | Ubuntu 22.04 LTS |

## Software Environment

| Package | Version |
|---------|---------|
| Python | 3.10 |
| CUDA | 11.8 |
| PyTorch | 2.1.0 |
| torchvision | 0.16.0 |
| lpips | 0.1.4 |
| numpy | 1.24+ |
| opencv-python | 4.8+ |

## Evaluation Protocol

1. **Train-test split**: Use dataset-provided standard splits. For Drum Tower: 134 train / 15 val / 56 test.
2. **Resolution**: Evaluate at native rendering resolution (matching ground-truth).
3. **Random seeds**: Fix random seed = 42 for all methods.
4. **Metrics computation**: All methods evaluated with identical metric code (`scripts/compute_stats.py`) to avoid implementation bias.
5. **Warm-up**: 2 warm-up render passes before FPS measurement.
6. **VRAM**: Measured at peak GPU memory usage during rendering (not training).

## Reproducibility Checklist

- [ ] Identical hardware for all experiments
- [ ] Fixed CUDA / PyTorch versions
- [ ] Standard train/test split
- [ ] Consistent metric implementation
- [ ] Public code and dataset links
- [ ] Zenodo DOI for permanent archiving
