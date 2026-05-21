"""Compute all evaluation metrics for 3DGS benchmark results.

Usage:
    python compute_stats.py --results_dir ../results/ --output ../results/all_results.csv
"""
import os
import csv
import glob
import argparse
from pathlib import Path

import numpy as np
import torch
from skimage.metrics import structural_similarity as ssim
import lpips


def compute_psnr(img_pred: np.ndarray, img_gt: np.ndarray) -> float:
    """Compute PSNR between two images in [0, 1] or [0, 255]."""
    mse = np.mean((img_pred - img_gt) ** 2)
    if mse == 0:
        return float("inf")
    if img_pred.max() <= 1.0:
        return 10 * np.log10(1.0 / mse)
    else:
        return 20 * np.log10(255.0 / np.sqrt(mse))


def compute_ssim(img_pred: np.ndarray, img_gt: np.ndarray) -> float:
    """Compute SSIM between two RGB images."""
    return ssim(
        img_pred, img_gt,
        channel_axis=2,
        data_range=img_gt.max() - img_gt.min()
    )


def compute_lpips(img_pred: np.ndarray, img_gt: np.ndarray, lpips_fn) -> float:
    """Compute LPIPS between two RGB images."""
    # Convert to [0, 1] and HWC -> CHW -> BCHW
    if img_pred.max() > 1.0:
        img_pred = img_pred / 255.0
        img_gt = img_gt / 255.0
    pred_tensor = torch.from_numpy(img_pred).permute(2, 0, 1).unsqueeze(0).float()
    gt_tensor = torch.from_numpy(img_gt).permute(2, 0, 1).unsqueeze(0).float()
    with torch.no_grad():
        return lpips_fn(pred_tensor, gt_tensor).item()


def compute_all_metrics(results_dir: str, output_csv: str):
    """Compute and save all metrics for all methods."""
    results = []
    methods = sorted(os.listdir(results_dir))

    lpips_fn = lpips.LPIPS(net="vgg").eval()

    for method in methods:
        method_dir = os.path.join(results_dir, method)
        if not os.path.isdir(method_dir):
            continue

        gt_dir = os.path.join(method_dir, "gt")
        pred_dir = os.path.join(method_dir, "pred")
        if not os.path.exists(gt_dir) or not os.path.exists(pred_dir):
            continue

        gt_files = sorted(glob.glob(os.path.join(gt_dir, "*.png")))
        pred_files = sorted(glob.glob(os.path.join(pred_dir, "*.png")))

        psnr_list, ssim_list, lpips_list = [], [], []
        for gt_path, pred_path in zip(gt_files, pred_files):
            gt_img = _load_image(gt_path)
            pred_img = _load_image(pred_path)

            psnr_list.append(compute_psnr(pred_img, gt_img))
            ssim_list.append(compute_ssim(pred_img, gt_img))
            lpips_list.append(compute_lpips(pred_img, gt_img, lpips_fn))

        results.append({
            "method": method,
            "psnr_mean": np.mean(psnr_list),
            "psnr_std": np.std(psnr_list),
            "ssim_mean": np.mean(ssim_list),
            "ssim_std": np.std(ssim_list),
            "lpips_mean": np.mean(lpips_list),
            "lpips_std": np.std(lpips_list),
            "num_images": len(gt_files),
        })

    # Save to CSV
    output_path = Path(output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["method", "psnr_mean", "psnr_std", "ssim_mean", "ssim_std",
                  "lpips_mean", "lpips_std", "num_images"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Saved results to {output_path}")
    return results


def _load_image(path: str) -> np.ndarray:
    """Load image as numpy float array in [0, 1]."""
    from PIL import Image
    img = Image.open(path).convert("RGB")
    return np.array(img).astype(np.float64) / 255.0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute benchmark metrics")
    parser.add_argument("--results_dir", type=str, default="../results/",
                        help="Directory containing per-method results")
    parser.add_argument("--output", type=str, default="../results/all_results.csv",
                        help="Output CSV file")
    args = parser.parse_args()
    compute_all_metrics(args.results_dir, args.output)
