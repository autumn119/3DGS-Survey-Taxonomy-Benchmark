"""Generate paper-quality figures from benchmark results.

Usage:
    python plot_metrics.py --results ../results/all_results.csv --output ../figures/
"""
import argparse
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 13,
    "figure.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})

METRICS = ["psnr_mean", "ssim_mean", "lpips_mean"]
METRIC_LABELS = {
    "psnr_mean": "PSNR (dB) ↑",
    "ssim_mean": "SSIM ↑",
    "lpips_mean": "LPIPS ↓",
}

COLORS = sns.color_palette("Set2", n_colors=20)


def plot_comparison_chart(results_csv: str, output_dir: str):
    """Generate bar charts comparing methods across metrics."""
    df = pd.read_csv(results_csv)
    df = df.sort_values("psnr_mean", ascending=True)

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for ax, metric in zip(axes, METRICS):
        values = df[metric].values
        errors = df[metric.replace("_mean", "_std")].values
        bars = ax.barh(df["method"], values, xerr=errors,
                       color=COLORS[:len(df)], capsize=3, alpha=0.85)
        ax.set_xlabel(METRIC_LABELS[metric])
        ax.set_title(f"{metric.replace('_mean', '').upper()}")
        # Add value labels on bars
        for bar, val in zip(bars, values):
            ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2,
                    f"{val:.2f}", va="center", fontsize=9)

    fig.suptitle("3DGS Benchmark: Method Comparison", fontsize=16, y=1.02)
    plt.tight_layout()
    output_path = f"{output_dir}/benchmark_comparison.png"
    plt.savefig(output_path, dpi=200)
    plt.close()
    print(f"Saved comparison chart to {output_path}")


def plot_radar_chart(results_csv: str, output_dir: str):
    """Generate radar chart for multi-dimensional comparison."""
    df = pd.read_csv(results_csv)
    df = df.set_index("method")

    # Normalize to [0, 1] for radar plot
    norm_scores = {}
    for metric in METRICS:
        values = df[metric].values
        min_v, max_v = values.min(), values.max()
        if metric == "lpips_mean":  # lower is better
            norm_scores[metric] = (max_v - values) / (max_v - min_v + 1e-8)
        else:
            norm_scores[metric] = (values - min_v) / (max_v - min_v + 1e-8)

    # Radar chart
    labels = ["PSNR", "SSIM", "LPIPS (1-LPIPS)"]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for i, method in enumerate(df.index):
        values = [norm_scores["psnr_mean"][i],
                  norm_scores["ssim_mean"][i],
                  norm_scores["lpips_mean"][i]]
        values += values[:1]
        ax.plot(angles, values, "o-", linewidth=2, label=method, color=COLORS[i])
        ax.fill(angles, values, alpha=0.1, color=COLORS[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("3DGS Method Radar Comparison", pad=20, fontsize=14)
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
    output_path = f"{output_dir}/radar_comparison.png"
    plt.savefig(output_path, dpi=200)
    plt.close()
    print(f"Saved radar chart to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate benchmark plots")
    parser.add_argument("--results", type=str, default="../results/all_results.csv",
                        help="Path to all_results.csv")
    parser.add_argument("--output", type=str, default="../figures/",
                        help="Output directory for figures")
    args = parser.parse_args()

    import os
    os.makedirs(args.output, exist_ok=True)

    plot_comparison_chart(args.results, args.output)
    plot_radar_chart(args.results, args.output)
    print("All plots generated successfully!")
