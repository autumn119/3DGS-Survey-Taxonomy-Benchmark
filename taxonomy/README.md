# Taxonomy Documentation

## Overview

This directory contains the hierarchical classification of 3D Gaussian Splatting methods, organized along two orthogonal dimensions:

1. **Task / Application Axis** — What the method is designed to achieve
2. **Technical Module Axis** — Which core components are modified or enhanced

The taxonomy follows the framework established by [awesome-3DGS (arXiv:2407.17418)](https://arxiv.org/abs/2407.17418) and the SoTA Point Cloud taxonomy structure.

## Classification Axes

### Axis 1: Task & Application

| Level 1 | Level 2 | Level 3 (Examples) |
|---------|---------|---------------------|
| **1. Original Proposal** | 3D Gaussian Splatting | — |
| **2. Optimization** | Storage Efficiency | Scaffold-GS, LightGaussian, Compact3D |
| | Training Efficiency | DISTWAR, I3DGS |
| | Rendering Efficiency | GSCore, RadSplat, StopThePop |
| | Photorealism | Mip-Splatting, GaussianShader, FreGS |
| **3. Generalization** | Generalizable (few-shot / zero-shot) | pixelSplat, MVSplat, Splatter Image |
| | Sparse View | FSGS, DNGaussian, GaussianObject |
| **4. Applications** | Human Reconstruction | GauHuman, 3DGS-Avatar (body), GaussianAvatars (head) |
| | AIGC (Text→3D, Image→3D) | DreamGaussian, LGM, LucidDreamer |
| | 4D Generation | DreamGaussian4D, GaussianFlow |
| | Autonomous Driving & SLAM | Street Gaussians, SplaTAM, GS-SLAM |
| **5. Extensions** | Dynamic Scenes | 4D GS, Deformable 3DGS, 3DGStream |
| | Surface Reconstruction | SuGaR, 2D GS, Gaussian Surfels |
| | Editable / Relightable | GaussianEditor, Relightable 3DGS |
| | Physics Simulation | PhysGaussian |

### Axis 2: Technical Module

| Module | Description | Representative Works |
|--------|-------------|---------------------|
| **Initialization** | SfM point cloud, voxel grid, mesh-based | Original 3DGS, Scaffold-GS |
| **Attribute Expansion** | Adding new Gaussian properties (SH coefficients, opacity, etc.) | Mip-Splatting, GaussianShader |
| **Splatting** | Rendering pipeline modifications (sorting, rasterization) | DISTWAR, StopThePop |
| **3D Regularization** | Depth, geometry, normal priors | SuGaR, 2D GS |
| **2D Regularization** | Frequency, perceptual, adversarial losses | FreGS |
| **Pruning & Densification** | Adaptive control of Gaussian count | LightGaussian, Compact3D |
| **Post-Processing** | Mesh extraction, relighting, mesh baking | SuGaR |
| **Integration** | Hybrid with PointCloud, Mesh, Triplane representations | Triplane Meets GS, GSDF |

## File Format

- **`3dgs_taxonomy.csv`**: Machine-readable CSV with columns:
  - `Method`: Method name
  - `Category_1`: Top-level category (Task or Technical)
  - `Category_2`: Second-level class
  - `Category_3`: Third-level (optional)
  - `Module_Focus`: Primary technical innovation
  - `Paper_Link`: arXiv or publication URL
  - `Code_Link`: GitHub repository URL
