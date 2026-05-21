# 评测指标实现

本目录包含统一的评测指标实现，确保所有方法的指标计算方式一致。

## 指标

| 指标 | 源文件 | 引用 |
|------|--------|------|
| PSNR | `compute_stats.py` 中的 `compute_psnr()` | MSE-based |
| SSIM | `skimage.metrics.structural_similarity` | Wang et al., 2004 |
| LPIPS | `lpips.LPIPS(net="vgg")` | Zhang et al., 2018 |

## 使用

```bash
python ../scripts/compute_stats.py --results_dir ../results/ --output ../results/all_results.csv
```
