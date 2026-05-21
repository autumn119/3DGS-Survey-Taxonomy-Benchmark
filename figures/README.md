# Paper Figures — Source Files

This directory contains all figures used in the survey paper.

## Included Figures

| Filename | Description | Format |
|----------|-------------|--------|
| `taxonomy_reference.png` | Reference taxonomy structure from SoTA-Point-Cloud (Guo et al., TPAMI 2020) | PNG |
| `taxonomy_figure.*` | 3DGS method classification hierarchy | PDF / PNG / SVG |
| `timeline.*` | Chronological development of 3DGS methods | PDF / PNG / SVG |
| `benchmark_comparison.png` | Bar chart comparing methods across metrics | PNG (script-generated) |
| `radar_comparison.png` | Multi-dimensional radar chart | PNG (script-generated) |

## Generation Commands

Figures can be (re)generated from benchmark results:

```bash
# Generate all comparison figures
cd ../scripts
python plot_metrics.py --csv ../results/all_results.csv --output_dir ../figures/
```

### Manual Figure Creation

- **Taxonomy figure**: Recommend using draw.io / TikZ / matplotlib
- **Timeline figure**: Recommend using matplotlib timeline visualization
- **Template**: `taxonomy_reference.png` provides a visual reference for the desired structure

## Notes

- All figures should be exported in both **PDF** (vector) and **PNG** (raster) formats
- High-resolution (300+ DPI) PNG versions for publication
- Source files (`.drawio`, `.tex`, `.py`) should be preserved alongside rendered outputs
