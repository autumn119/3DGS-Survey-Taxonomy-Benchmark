# 论文图表源文件

## 包含的图表

| 文件名 | 说明 | 格式 |
|--------|------|------|
| `taxonomy_figure.*` | 3DGS方法分类体系层级图 | PDF / PNG / SVG |
| `timeline.*` | 3DGS方法发展时间线图 | PDF / PNG / SVG |
| `benchmark_comparison.png` | 各方法基准对比柱状图 | PNG (脚本生成) |
| `radar_comparison.png` | 多维度雷达图对比 | PNG (脚本生成) |

## 生成命令

```bash
# 运行脚本生成图表（需要有 results/all_results.csv）
cd ../scripts
python plot_metrics.py
```
