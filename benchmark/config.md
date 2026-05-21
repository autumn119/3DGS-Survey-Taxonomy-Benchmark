# 基准评测配置

## 数据集 (Datasets)

| 数据集 | 场景数 | 分辨率 | 训练/测试帧 | 用途 |
|--------|--------|--------|-------------|------|
| Mip-NeRF 360 | 9 | 1600×1200 | 按官方划分 | 前向/360°场景 |
| Tanks & Temples | 21 | 1920×1080 | 每7帧取1帧 | 大规模室外 |
| Deep Blending | 2 | 1920×1080 | 按官方划分 | 复杂光照 |
| Synthetic NeRF | 8 | 800×800 | 100训练/200测试 | 合成物体 |
| 鼓楼场景 (自定义) | 3 | 400×400 | 134训练/56测试 | 传统建筑 |

## 评测指标 (Metrics)

| 指标 | 全称 | 计算方式 | 说明 |
|------|------|----------|------|
| PSNR | Peak Signal-to-Noise Ratio | `10 * log10(1.0 / MSE)` | 像素级重建质量 |
| SSIM | Structural Similarity | `skimage.metrics.structural_similarity` | 结构一致性 |
| LPIPS | Learned Perceptual Image Patch Similarity | AlexNet/VGG backbone | 感知相似度 |
| FPS | Frames Per Second | 渲染帧数 / 渲染时间 | 推理速度 |
| VRAM | GPU Memory | `torch.cuda.max_memory_allocated()` | 显存占用 |
| Train Time | 训练时间 | 总训练耗时 | 训练效率 |

## 硬件环境 (Hardware)

| 组件 | 规格 |
|------|------|
| GPU | NVIDIA RTX 4090 (24GB) |
| CPU | Intel Xeon |
| RAM | 64GB |
| OS | Ubuntu 20.04 LTS |

## 软件环境 (Software)

| 组件 | 版本 |
|------|------|
| Python | 3.8 |
| PyTorch | 1.13.1 |
| CUDA | 11.7 |
| 3DGS diff-gaussian-rasterization | latest |

## 评测协议 (Evaluation Protocol)

1. **公平对比原则**: 所有方法在同一数据集划分、相同分辨率下评估
2. **超参数**: 各方法使用原论文推荐的默认超参数
3. **迭代次数**: 统一 30,000 次迭代
4. **随机种子**: 固定 random seed = 42
5. **指标计算**: 使用 `scripts/compute_metrics.py` 统一计算，避免不同实现差异
6. **多次运行**: 每个方法运行 3 次，取平均值

## 复现命令

```bash
# 以 3DGS 原版为例
git clone https://github.com/graphdeco-inria/gaussian-splatting
cd gaussian-splatting
conda activate 3dgs

# 训练
python train.py -s /path/to/dataset -m output/model_name --iterations 30000

# 渲染
python render.py -m output/model_name --skip_train

# 评估
python metrics.py -m output/model_name
```
