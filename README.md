# ROS2 Autonomous Perception Stack — High-Level Plan

## Overview
Build a real-time autonomous perception pipeline using:
- ROS2
- CARLA Simulator
- YOLO-based object detection
- Edge inference optimization
- Semantic segmentation
- Sensor fusion
- ViT-based perception models

---

# Phase 1 — Setup

## Tasks
- Install ROS2 and CARLA
1. CARLA 0.9.15
2. WSL2 DistroUbuntu 22.04 LTS (installed)
3. ROS VersionROS2 Humble
4. ros-bridge branch/tag for 0.9.15

- Setup Python/C++ environment
- Connect CARLA sensors with ROS2

## Deliverable
- CARLA sensor data published to ROS2 topics

---

# Phase 2 — Object Detection

## Tasks
- Integrate pretrained YOLO model
- Run real-time detection on CARLA camera stream
- Visualize detections in ROS2

## Deliverable
- Real-time object detection pipeline

---

# Phase 3 — Modular ROS2 Pipeline

## Tasks
- Create separate ROS2 nodes
- Add launch/config files
- Add basic C++ integration

## Deliverable
- Modular ROS2 perception stack

---

# Phase 4 — Performance Benchmarking

## Comparison
- CPU vs GPU
- FP32 vs FP16
- TensorRT optimized inference

## Metrics
- FPS
- Latency
- GPU/CPU usage

## Deliverable
- Benchmark report and performance comparison

---

# Phase 5 — Edge Inference

## Tasks
- Convert model to ONNX/TensorRT
- Apply quantization (FP16/INT8)
- Run optimized inference on edge device

## Deliverable
- Real-time optimized edge inference pipeline

---

# Phase 6 — Semantic Segmentation

## Tasks
- Add drivable-area/terrain segmentation
- Integrate segmentation into ROS2 pipeline

## Deliverable
- Detection + segmentation perception pipeline

---

# Phase 7 — Sensor Fusion

## Tasks
- Add LiDAR sensor in CARLA
- Fuse RGB camera + LiDAR information
- Estimate object distance and scene understanding

## Deliverable
- Basic camera + LiDAR fusion pipeline

---

# Phase 8 — ViT-Based Detection Extension

## Tasks
- Integrate transformer-based detector

## Comparison
- Accuracy
- FPS
- Latency
- Edge suitability

## Deliverable
- CNN vs ViT perception comparison

---

# Final Deliverables

- GitHub repository
- Demo video
- Benchmark report
- ROS2 modular perception stack
- CNN vs ViT comparison
