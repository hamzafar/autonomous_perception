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
- changing wsl ntwork mode from Mirrored to NAT also contributed in reducing memory ~6GB and overall ~5fps gain

### Key Benchmark Results

| Configuration | Throughput |
|---------------|------------|
| Single Publisher | ~3 FPS |
| Multi-Thread DDS Publisher | ~15 FPS |
| Improvement | ~5× |


## Deliverable
- Results of multi-threaded fps optimization

---
# Phase 6 — Model Compression & Perception Optimization

## Tasks

### Baseline Benchmarking

* Benchmark YOLOv8m-seg PyTorch FP32
* Measure baseline perception performance
* Measure baseline resource utilization

### Model Compression & Acceleration

* Benchmark PyTorch FP16 inference
* Export YOLOv8m-seg to ONNX (completed)
* Benchmark ONNX Runtime GPU inference
* Export TensorRT FP16 engine (completed)
* Benchmark TensorRT FP16 inference
* Export TensorRT INT8 engine (completed)
* Benchmark TensorRT INT8 inference (completed)
* Compare runtime performance improvements (completed)
* Compare resource utilization (completed)

### Consistency Analysis

* Use FP32 predictions as reference (completed)
* Compare TensorRT FP16 predictions against FP32 (completed)
* Compare TensorRT INT8 predictions against FP32 (completed)
* Measure detection agreement (completed)
* Measure class agreement (completed)
* Measure localization consistency (completed)

### Pipeline Profiling

* Measure image preprocessing time (completed)
* Measure inference time (completed)
* Measure rendering time (completed)
* Measure display overhead (completed)
* Measure total pipeline latency (completed)
* Identify dominant bottlenecks (completed)

### Architecture Optimization

* Investigate rendering bottlenecks (completed)
* Evaluate display-thread separation (completed)
* Implement threaded rendering architecture (completed)
* Measure throughput improvements (completed)

### Benchmark Analysis

* Compare FP32, FP16, and TensorRT INT8 (completed)
* Evaluate speed versus consistency trade-offs (completed)
* Compare resource utilization (completed)
* Compare latency improvements (completed)
* Identify remaining bottlenecks (completed)

---

## Completed

### Baseline Benchmarking

* ✅ PyTorch FP32 benchmarking
* ✅ PyTorch FP16 benchmarking
* ✅ Resource utilization analysis

### Model Compression & Acceleration

* ✅ ONNX export
* ✅ ONNX Runtime GPU configuration
* ✅ ONNX Runtime GPU evaluation
* ✅ TensorRT installation and configuration
* ✅ TensorRT FP16 engine export
* ✅ TensorRT FP16 benchmarking
* ✅ INT8 calibration dataset creation
* ✅ TensorRT INT8 engine export
* ✅ TensorRT INT8 benchmarking

### Consistency Analysis

* ✅ FP32 vs TensorRT FP16 comparison
* ✅ FP32 vs TensorRT INT8 comparison
* ✅ Detection agreement analysis
* ✅ Class agreement analysis
* ✅ Bounding-box IoU analysis

### Pipeline Profiling

* ✅ Preprocessing profiling
* ✅ Inference profiling
* ✅ Rendering profiling
* ✅ Display profiling
* ✅ End-to-end pipeline profiling

### Architecture Optimization

* ✅ Rendering bottleneck investigation
* ✅ Display-thread evaluation
* ✅ Threaded rendering implementation
* ✅ Throughput optimization

---

## Current Findings

### PyTorch FP32 Baseline

Steady-state performance:

* Avg FPS: 10.16

### TensorRT FP16

Steady-state performance:

* Avg FPS: 26.33

Findings:

* Significant throughput improvement over FP32
* High prediction consistency retained

### TensorRT INT8

Steady-state performance:

* Avg FPS: 26.81

Findings:

* Highest throughput achieved
* Best efficiency-performance trade-off
* Lower prediction consistency than FP16

### ONNX Runtime GPU

Findings:

* Successfully deployed under WSL2
* Required manual CUDA/cuDNN configuration
* Evaluated as intermediate deployment format

### ONNX Runtime INT8

Findings:

* Dynamic INT8 quantization generated successfully
* GPU execution failed due to unsupported ConvInteger operators
* Not suitable for YOLOv8-seg INT8 deployment

---

### Calibration Dataset

Created from CARLA replay recordings.

Dataset:

* 500 representative images

Used for:

* TensorRT INT8 engine calibration

---

## Consistency Analysis

Dataset:

* 900 replay images

### FP32 vs TensorRT FP16

| Metric | Value |
|----------|---------:|
| Detection Agreement | 94.75% |
| Class Agreement | 97.77% |
| Mean Box IoU | 0.976 |

### FP32 vs TensorRT INT8

| Metric | Value |
|----------|---------:|
| Detection Agreement | 90.23% |
| Class Agreement | 95.41% |
| Mean Box IoU | 0.943 |

### Key Findings

* FP16 preserved predictions better than INT8
* INT8 introduced measurable consistency loss
* Localization quality remained high for both models

---

## Pipeline Profiling

Dataset:

* 900 replay images

| Component | FP32 | FP16 | INT8 |
|------------|---------:|---------:|---------:|
| Preprocessing | 0.35 ms | 0.37 ms | 0.37 ms |
| Inference | 44.94 ms | 31.55 ms | 24.79 ms |
| Rendering | 14.27 ms | 14.72 ms | 15.90 ms |
| Display | 4.71 ms | 4.67 ms | 4.67 ms |
| Total Pipeline | 64.27 ms | 51.31 ms | 45.91 ms |

### Key Findings

* TensorRT significantly reduced inference latency
* Rendering became a major bottleneck
* Visualization cost became comparable to inference cost
* Inference was no longer the sole bottleneck

---

## Architecture Optimization

### Original Architecture

Callback Thread:

* Inference
* Rendering
* FPS Overlay

Display Thread:

* OpenCV Display

### Optimized Architecture

Callback Thread:

* Inference Only

Display Thread:

* Rendering
* FPS Overlay
* OpenCV Display

### Results

| Model | Avg FPS |
|---------|---------:|
| FP32 | 10.16 |
| TensorRT FP16 | 26.33 |
| TensorRT INT8 | 26.81 |

### Key Findings

* Rendering blocked callback execution
* Threaded rendering enabled pipeline parallelism
* TensorRT pipelines benefited significantly from architecture optimization

---

## End-to-End Comparison

| Configuration | Avg FPS |
|---------------|---------:|
| Live CARLA + ROS2 + YOLOv8m-seg | ~3.5 |
| Replay + TensorRT INT8 | ~26 |

Improvement:

* Approximately 7.4× higher throughput

---

## Deliverables

### Performance Comparison

| Precision | Avg FPS |
|------------|---------:|
| FP32 | 10.16 |
| TensorRT FP16 | 26.33 |
| TensorRT INT8 | 26.81 |

### Consistency Comparison

| Precision | Detection Agreement | Class Agreement | Mean Box IoU |
|------------|------------------:|--------------:|------------:|
| TensorRT FP16 | 94.75% | 97.77% | 0.976 |
| TensorRT INT8 | 90.23% | 95.41% | 0.943 |

### Pipeline Profiling

| Component | Time (ms) |
|------------|----------:|
| Preprocessing | 0.35–0.37 |
| Inference | 24.79–44.94 |
| Rendering | 14.27–15.90 |
| Display | 4.67–4.71 |
| Total Pipeline | 45.91–64.27 |


---

# Phase 7 — Sensor Fusion & 3D Perception Foundations

## Objectives

Extend the perception stack beyond monocular vision by integrating LiDAR data and basic sensor fusion techniques.


## 7.1 LiDAR Integration

### Tasks

- Add LiDAR sensor to CARLA vehicle
- Publish LiDAR point clouds through ROS2
- Visualize point cloud data
- Validate camera-LiDAR synchronization

### Focus Areas

- Point cloud processing
- ROS2 sensor integration
- Multi-sensor synchronization


## 7.2 Camera–LiDAR Calibration

### Tasks

- Extract camera intrinsic parameters
- Extract LiDAR extrinsic parameters
- Transform LiDAR points into camera coordinates
- Project LiDAR points onto image plane

### Goal

Create a unified camera-LiDAR representation.


## 7.3 2D–3D Association

### Tasks

- Run YOLOv8 perception pipeline
- Associate LiDAR points with detected objects
- Filter object-specific point clusters
- Estimate object distance

### Outputs

- Object Class
- Bounding Box
- Estimated Distance

### Example

Car: 18.4 m

Truck: 27.1 m

Pedestrian: 12.3 m


## 7.4 Sensor Fusion Pipeline

### Tasks

- Fuse camera detections with LiDAR measurements
- Generate distance-aware detections
- Evaluate fusion robustness
- Analyze fusion performance

### Focus Areas

- Multi-modal perception
- Detection enhancement
- Scene understanding


## 7.5 3D Perception Foundations

### Tasks

- Generate Bird's-Eye View representation
- Visualize projected point clouds
- Estimate object positions
- Build spatial awareness pipeline

### Goal

Transition from 2D perception toward 3D scene understanding.


## 7.6 Benchmarking & Analysis

### Comparison

| Pipeline | Detection | Distance Estimation | Spatial Awareness |
|-----------|-----------|-----------|-----------|
| Camera Only | ✓ | ✗ | Limited |
| Camera + LiDAR | ✓ | ✓ | Improved |

### Metrics

- Distance estimation accuracy
- Sensor synchronization stability
- Fusion processing latency
- Perception throughput


## Deliverables

- ROS2 LiDAR integration
- Camera-LiDAR calibration pipeline
- Distance-aware object detection
- Sensor fusion perception pipeline
- Basic 3D perception framework
- Fusion benchmarking report
- Multi-modal perception demonstration


## Outcome

Transition from camera-only perception toward multi-modal robotics perception.
---

# Phase 8 — Multi-Camera Perception

## Objectives

Expand perception coverage using multiple synchronized cameras.


## Scope

### Camera Configuration

- Front camera
- Rear camera
- Left camera
- Right camera

### Tasks

- Multi-camera ROS2 integration
- Camera synchronization
- Multi-stream visualization
- Cross-camera object tracking
- Overlapping field-of-view analysis
- Unified perception visualization

### Focus Areas

- 360° scene awareness
- Multi-camera architecture
- Perception scalability
- Sensor synchronization


## Deliverables

- Multi-camera ROS2 pipeline
- 360° perception visualization
- Multi-camera benchmarking report
- Multi-camera perception demonstration


## Outcome

Expand perception coverage from a single viewpoint to full-surround awareness.

---
# Phase 9 — Advanced Multi-Modal Perception

## Objectives

Combine camera, LiDAR, and multi-camera perception into a unified perception system.


## Scope

### Tasks

- Multi-camera and LiDAR synchronization
- Multi-modal data association
- Bird's-Eye View generation
- Unified world representation
- Object localization in world coordinates
- Scene-level perception analysis

### Focus Areas

- Advanced sensor fusion
- 3D scene understanding
- Spatial reasoning
- Autonomous perception architecture


## Deliverables

- Multi-camera + LiDAR fusion pipeline
- Bird's-Eye View visualization
- Unified perception framework
- Multi-modal benchmarking report


## Outcome

Build a complete multi-modal perception stack resembling modern autonomous systems.

---

# Phase 10 — Edge Inference Readiness & Deployment

## Objectives

Deploy the optimized perception stack on embedded edge hardware.


## Target Platforms

- NVIDIA Jetson Nano
- NVIDIA Jetson Xavier NX
- NVIDIA Jetson Orin Nano


## 10.1 Deployment Preparation

### Tasks

- Containerize perception pipeline
- Prepare deployment scripts
- Package ROS2 perception nodes
- Validate TensorRT deployment workflow


## 10.2 Edge Optimization

### Tasks

- Optimize memory usage
- Optimize power consumption
- Tune TensorRT inference settings
- Analyze thermal behavior
- Evaluate deployment constraints


## 10.3 Edge Benchmarking

### Comparison

| Platform | FPS | Latency | GPU Utilization | Memory Usage |
|-----------|-----|----------|----------------|--------------|
| Desktop GPU | | | | |
| Jetson Nano | | | | |
| Xavier NX | | | | |
| Orin Nano | | | | |

### Metrics

- Real-time FPS
- End-to-end latency
- Memory footprint
- Power efficiency
- Thermal stability


## 10.4 Deployment Validation

### Tasks

- Continuous perception testing
- Long-duration stability testing
- Resource monitoring
- Failure analysis


## Deliverables

- Edge deployment workflow
- TensorRT deployment package
- Containerized perception stack
- Edge benchmarking report
- Embedded deployment guide


## Outcome

Deploy a robotics perception system on real edge hardware with validated real-time performance.

---
# Phase 11 — ViT-Based Detection Extension

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
