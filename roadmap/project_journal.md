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

- CARLA resource utilization analysis (completed)
- CPU, RAM, GPU, VRAM benchmarking (completed)
- Traffic and YOLO workload profiling (completed)

### Sensor Throughput Analysis

- RGB camera resolution profiling (completed)
- Camera FPS benchmarking (completed)
- ROS Bridge throughput investigation (completed)

### Dataset Recording

- Direct CARLA image recording (completed)
- Timestamped dataset generation (completed)
- Fixed-frame dataset generation (completed)
- Queue-based asynchronous recording (completed)
- Deterministic synchronous recording (completed)

### Offline Replay Pipeline

- Dataset replay viewer (completed)
- Replay FPS validation (completed)
- Replay without CARLA (completed)

### Replay Publisher Pipeline

- ROS2 image replay publisher (completed)
- Replay-based perception benchmarking (completed)
- Offline YOLO evaluation (completed)

### Dataset Utilities

- Dataset resizing pipeline (completed)
- Multi-resolution dataset generation (completed)

## Completed

- ✅ Hardware profiling framework
- ✅ CPU, RAM, GPU, VRAM benchmarking
- ✅ Camera throughput profiling
- ✅ Direct CARLA recorder
- ✅ Queue-based recording architecture
- ✅ Deterministic synchronous recorder
- ✅ Timestamped dataset generation
- ✅ Fixed-frame dataset generation
- ✅ Offline replay viewer
- ✅ Offline replay publisher
- ✅ Replay-based perception testing
- ✅ Offline YOLO evaluation
- ✅ Dataset resizing utility
- ✅ Tick-to-image synchronization validation
- ✅ 100/100 synchronized capture validation
- ✅ 900/900 synchronized capture validation
- ✅ Zero-frame-loss recording pipeline
- ✅ Traffic manager integration validation


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
## Phase 5 — ROS2 Transport Performance Investigation

### Tasks

- Validate DDS large message transport (completed)
- Benchmark ROS2 image streaming (completed)
- Measure publisher/subscriber throughput (completed)
- Evaluate OpenCV visualization impact (completed)
- Investigate single-stream limitations (completed)
- Investigate multi-stream scaling (completed)
- Evaluate DDS throughput limits (completed)
- Investigate QoS configurations (completed)
- Investigate publisher-side multithreading (completed)
- Validate ROS2 image replay from recorded CARLA datasets (completed)
- Validate YOLOv8m-seg inference on ROS2 image streams (completed)

### Completed

- ✅ DDS transport validated with 16 MB, 32 MB, and 64 MB payloads

- ✅ ROS2 image transport benchmark created

- ✅ OpenCV visualization isolated from transport testing

- ✅ Subscriber processing overhead isolated

- ✅ Aggregate throughput validated above 20 FPS

- ✅ Multi-publisher scaling validated (up to 7 publishers @ 3 FPS)

- ✅ Single high-rate publisher limitations identified

- ✅ Multi-threaded publisher prototype validated

- ✅ Multi-threaded DDS publishing increased throughput from ~3 FPS to ~15 FPS

- ✅ Offline CARLA dataset replay integrated with ROS2

- ✅ End-to-end CARLA Replay → ROS2 → OpenCV pipeline validated

- ✅ End-to-end CARLA Replay → ROS2 → YOLOv8m-seg pipeline validated

-✅ QoS experimentation completed

### Current Findings

- DDS successfully handles large payload transport.
- Large payloads introduce additional latency.
- CPU is not the primary bottleneck.
- Aggregate throughput scales beyond 20 FPS.
- Multiple low-rate publishers outperform a single high-rate publisher.
- Publisher-side multithreading improves aggregate throughput by approximately 5×.
- Single publisher throughput was limited to approximately 3 FPS.
- Multi-threaded DDS publishing achieved approximately 15 FPS aggregate throughput.
- ROS2 image transport is suitable for real-time perception workloads on consumer hardware.
- End-to-end replay → ROS2 → YOLOv8m-seg perception remained stable at approximately 8–12 FPS.
- Bottleneck appears related to per-stream queueing and buffering rather than overall DDS bandwidth.
- Current limitations appear primarily hardware-related (RAM, VRAM, and inference workload) rather than DDS transport stability.

### Key Benchmark Results

| Configuration | Throughput |
|---------------|------------|
| Single Publisher | ~3 FPS |
| Multi-Thread DDS Publisher | ~15 FPS |
| Improvement | ~5× |


## Deliverable
- Results of multi-threaded fps optimization

---
# Phase 6 — Model Compression & Pipeline Analysis
## Tasks

### Model Compression Benchmarking

- Benchmark YOLOv8m-seg FP32 baseline
- Benchmark YOLOv8m-seg FP16 inference
- Benchmark YOLOv8m-seg INT8 inference
- Compare model resource utilization
- Compare inference performance

### Consistency Analysis

- Use FP32 predictions as reference
- Compare FP16 predictions against FP32
- Compare INT8 predictions against FP32
- Measure prediction consistency after quantization

### Pipeline Profiling

- Measure ROS2 callback time
- Measure image preprocessing time
- Measure YOLO inference time
- Measure postprocessing time
- Measure OpenCV visualization overhead
- Measure total pipeline processing time

### Benchmark Analysis

- Evaluate compression trade-offs
- Compare runtime performance
- Compare resource utilization
- Compare prediction consistency
- Identify dominant perception pipeline stages

## Completed

## Current Findings

### FP32 Baseline

To be evaluated.

### FP16 Quantization

To be evaluated.

### INT8 Quantization

To be evaluated.

### Consistency Analysis

FP32 predictions will be used as the reference for evaluating FP16 and INT8 prediction consistency.

Metrics:

- IoU
- Precision
- Recall
- F1 Score

### Pipeline Profiling

Profiling will be used to understand where computation time is spent within the perception pipeline.

Target components:

- ROS2 callback
- Image preprocessing
- YOLO inference
- Postprocessing
- OpenCV visualization


### Deliverables

### Performance Comparison

| Precision | FPS | Inference Latency | CPU | GPU | RAM | VRAM |
|------------|------|------------------|------|------|------|------|
| FP32 | | | | | | |
| FP16 | | | | | | |
| INT8 | | | | | | |

### Consistency Comparison

| Precision | IoU | Precision | Recall | F1 Score |
|------------|------|-----------|--------|----------|
| FP16 | | | | |
| INT8 | | | | |

### Pipeline Profiling

| Component | Time (ms) |
|------------|-----------|
| ROS2 Callback | |
| Image Preprocessing | |
| YOLO Inference | |
| Postprocessing | |
| OpenCV Visualization | |
| Total Pipeline Time | |


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
