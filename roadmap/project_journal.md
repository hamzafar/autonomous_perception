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
1. Windows 11 CARLA 0.9.15 (installed)
2. WSL2 Ubuntu 22.04 (installed)
3. ROS2 Humble (installed)
4. CARLA ROS Bridge (installed)
5. DDS communication (installed)

- Setup Python/C++ environment (installed)
- Connect CARLA sensors with ROS2 (installed)
- Validate CARLA sensor streaming through ROS2 visualization (Configured)

## Completed
- ✅ Windows ↔ WSL2 networking
- ✅ CARLA ↔ ROS bridge connectivity
- ✅ ROS2 DDS communication
- ✅ WSL2 mirrored networking configuration
- ✅ CARLA bridge stability with 0.9.15
- ✅ ROS topics publishing
- ✅ Ego vehicle, camera, LiDAR, radar, IMU/GNSS integration
- ✅ ROS2 camera subscriber and OpenCV visualization pipeline
- ✅ End-to-end CARLA → ROS2 → OpenCV perception pipeline validation

## Deliverable
- CARLA sensor data published to ROS2 topics
  <p align="center">
  <img src="assets/gifs/phase1_pipeline.gif" width="600"/>
  </p>

  <p align="center">
  <b>Phase 1:</b> End-to-end CARLA → ROS2 → OpenCV perception pipeline validation with real-time RGB camera streaming on WSL2 Ubuntu 22.04.
</p>

---

# Phase 2 — Object Detection

## Tasks
- Enable ego vehicle autopilot (configured)
- Integrate pretrained YOLO model (configured)
- Run real-time detection on CARLA camera stream (configured)
- Visualize detections in ROS2 (configured)

## Completed
- ✅ Ego vehicle autopilot enabled through ROS2
- ✅ Moving scene visualization through OpenCV pipeline
- ✅ Pretrained YOLOv8 integrated with CARLA RGB stream
- ✅ Real-time object detection running through ROS2 pipeline
- ✅ OpenCV visualization with YOLO bounding boxes
- ✅ Dynamic scene perception validated using CARLA autopilot

## Deliverable
- Real-time object detection pipeline
<p align="center">
  <img src="assets/gifs/phase2_pipeline.gif" width="600"/>
</p>

<p align="center">
  <b>Phase 2:</b> Real-time YOLOv8 object detection on CARLA RGB stream using ROS2, OpenCV, and Python perception pipeline.
</p>

---

# Phase 3 — ROS2 Modular Architecture

## Tasks
- Convert standalone scripts into ROS2 package (done)
- Learn ROS2 package structure (done)
- Create reusable ROS2 nodes (done)
- Learn ROS2 launch system (done)
- Learn topic remapping (done)
- Learn ROS2 parameters (done)
- Add config-driven architecture (done)
- Understand ROS2 node lifecycle/debugging (done)

## Completed

- ✅ Standalone perception scripts converted into modular ROS2 package architecture
- ✅ ROS2 executable nodes configured using setup.py and colcon build system
- ✅ Multi-node ROS2 launch system implemented using .launch.py architecture
- ✅ Configurable reusable ROS2 perception nodes implemented using ROS parameters
- ✅ Topic remapping concepts implemented for modular node communication
- ✅ YAML-based config-driven ROS2 parameter architecture implemented
- ✅ ROS2 debugging and node/topic inspection workflow understood

## Deliverable
- Modular ROS2 perception package with launch-based deployment

<p align="center">
  <img src="assets/diagrams/ros_package_workflow2.png" width="800"/>
</p>

<p align="center">
  ROS2 modular perception architecture using CARLA, ROS2 launch system, configurable nodes, YAML-based parameters, and YOLOv8 inference pipeline.
</p>

---
# Phase 4 — Hardware Profiling & Offline Replay

## Tasks

### Hardware Profiling

Measure resource utilization for:

- CARLA only (completed)
- CARLA + ROS Bridge (completed)
- CARLA + Traffic (completed)
- CARLA + YOLO (completed)

Monitor:

- CPU utilization (completed)
- RAM utilization (completed)
- GPU utilization (completed)
- VRAM utilization (completed)
- Temperature (completed)
- Disk I/O (completed)

### Sensor Throughput Analysis

Evaluate perception throughput under different camera resolutions:

- 800×600 RGB camera profiling (completed)
- 640×480 RGB camera profiling (completed)
- 320×240 RGB camera profiling (completed)
- Camera FPS benchmarking (completed)
- ROS Bridge throughput investigation (completed)

### Dataset Recording

- Record RGB camera stream (completed)
- Save timestamped frames (completed)
- Evaluate ROS2 bag recording (completed)
- Evaluate frame-based recording (completed)
- Implement direct CARLA recorder (completed)
- Queue-based asynchronous image saving (completed)
- Fixed-size dataset generation (completed)

### Offline Replay Pipeline

- Implement image replay viewer (completed)
- Validate replay performance (completed)
- Replay perception data without CARLA (completed)

### Future Replay Publisher

- Publish saved frames as ROS2 image topics (completed)
- Replay-based perception benchmarking (completed)
- Offline YOLO evaluation pipeline (completed)

## Completed

- ✅ Hardware profiling framework
- ✅ CPU, RAM, GPU, VRAM benchmarking
- ✅ CARLA resource utilization analysis
- ✅ RGB camera throughput benchmarking
- ✅ Resolution-based FPS profiling
- ✅ Direct CARLA camera recording
- ✅ Queue-based recording architecture
- ✅ Timestamped dataset generation
- ✅ Fixed-frame dataset generation
- ✅ Offline image replay viewer
- ✅ Replay validation
- ✅ Zero-frame-loss recording pipeline
- ✅ Low-memory recording workflow
- ✅ offline replay publisher node
- ✅ Replay-based perception testing

## Deliverable

### Online Profiling

| Scenario | CPU | RAM | GPU |
|-----------|------|------|------|
| CARLA Only | 48% | ~8GB | 38% |
| CARLA + ROS Bridge | 65% | ~9GB | 40% |
| CARLA + Viewer | 70% | ~11GB | 40% |
| CARLA + YOLO | 75% | ~13.5GB | 60% |

### Offline Replay Profiling

| Scenario | CPU | RAM | GPU |
|-----------|------|------|------|
| Replay Publisher + Viewer | ~30% | ~8 GB | N/A |
| Replay Publisher + YOLO | ~30% | ~9.5 GB | ~30% |
  
---
# Phase 5 — Network Profiling and FPS Optimization

---
# Phase 6 — Real-Time Perception Optimization
## Tasks
- debug underlaying wsl ros2 data transfer system
- improve subcriber node fps

## Completed

## Deliverable
- Results of faster fps perception stack
---

## 6.1 Baseline Benchmarking

### Tasks

- Benchmark YOLOv8 inference on CPU
- Benchmark YOLOv8 inference on GPU
- Establish FP32 baseline performance

### Metrics

- FPS
- Inference latency
- End-to-end pipeline latency
- CPU utilization
- GPU utilization
- RAM usage
- VRAM usage

### Deliverables

- Baseline benchmark table
- Performance comparison graphs

---

## 6.2 FP16 Optimization

### Tasks

- Enable FP16 mixed precision inference
- Benchmark FP16 performance

### Comparison

- FP32 vs FP16

### Focus Areas

- FPS improvement
- Latency reduction
- VRAM reduction

---

## 6.3 INT8 Quantization

### Tasks

- Apply PTQ (Post-Training Quantization)
- Benchmark INT8 inference performance
- Evaluate memory footprint reduction

### Comparison

- FP32 vs FP16 vs INT8

### Focus Areas

- Edge deployment feasibility
- Accuracy vs performance tradeoffs
- Model size reduction

---

## 6.4 Pipeline Profiling

### Profiling Targets

- ROS2 callback latency
- Image preprocessing time
- YOLO inference time
- Postprocessing time
- OpenCV visualization overhead
- Total end-to-end pipeline latency

### Goal

Identify real-time bottlenecks in the perception pipeline.

---

## 6.5 Benchmark Analysis

### Metrics

- FPS
- Latency
- Memory usage
- Throughput stability
- Accuracy impact

### Deliverables

- Optimization benchmark report
- Performance graphs
- Profiling analysis
- Compression comparison tables

---

# Phase 7 — Edge Inference Readiness & Accelerated Deployment

## Objectives

Optimize the robotics perception pipeline for accelerated real-time inference and future edge deployment.

---

## 7.1 ONNX Conversion

### Tasks

- Convert YOLOv8 PyTorch model to ONNX
- Validate ONNX inference pipeline
- Benchmark ONNX Runtime performance

### Comparison

- PyTorch vs ONNX Runtime

### Focus Areas

- Runtime portability
- Faster inference execution
- Reduced deployment complexity

---

## 7.2 TensorRT Optimization

### Tasks

- Convert ONNX model to TensorRT engine
- Optimize TensorRT FP16 inference
- Explore TensorRT INT8 optimization (optional)

### Comparison

- PyTorch vs ONNX Runtime vs TensorRT

### Focus Areas

- GPU acceleration
- Low-latency inference
- Throughput optimization
- Real-time perception performance

---

## 7.3 Real-Time Pipeline Optimization

### Tasks

- Optimize ROS2 perception nodes
- Implement asynchronous inference pipeline
- Reduce frame drops
- Improve queue management
- Optimize preprocessing and postprocessing stages
- Reduce end-to-end pipeline latency

### Goal

Achieve stable real-time perception performance under continuous streaming workloads.

---

## 7.4 Edge Deployment Preparation

### Target Platforms

- NVIDIA Jetson Nano
- NVIDIA Jetson Orin Nano
- NVIDIA Xavier NX

### Tasks

- Prepare TensorRT-compatible deployment pipeline
- Validate edge-compatible model formats
- Benchmark optimized inference runtimes on desktop GPU
- Structure pipeline for future Jetson deployment
- Analyze deployment constraints for edge hardware

### Goal

Develop an edge-ready perception architecture for future embedded deployment.

---

## 7.5 Final Benchmarking & Analysis

### Comparison

| Backend | Precision | FPS | Latency | Memory Usage |
|----------|-----------|-----|----------|---------------|
| PyTorch | FP32 |  |  |  |
| PyTorch | FP16 |  |  |  |
| ONNX Runtime | FP32 |  |  |  |
| TensorRT | FP16 |  |  |  |
| TensorRT | INT8 |  |  |  |

### Metrics

- Real-time FPS
- End-to-end latency
- GPU utilization
- Throughput stability
- Memory footprint
- Inference efficiency

---

## Deliverables

- Accelerated real-time perception pipeline
- TensorRT optimized inference workflow
- ONNX/TensorRT benchmark report
- Edge-ready deployment architecture
- Real-time inference performance analysis

---

# Phase 8 — Sensor Fusion

## Tasks
- Add LiDAR sensor in CARLA
- Fuse RGB camera + LiDAR information
- Estimate object distance and scene understanding

## Deliverable
- Basic camera + LiDAR fusion pipeline

---

# Phase 9 — ViT-Based Detection Extension

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
