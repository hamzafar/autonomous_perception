# Phase 6 — Model Compression & Perception Optimization

## Objective

Optimize the robotics perception pipeline for real-time deployment through model compression, TensorRT acceleration, pipeline profiling, and architecture optimization.

This phase focused on benchmarking multiple inference backends, analyzing prediction consistency, identifying system bottlenecks, and improving end-to-end perception throughput.

---

## Architecture

```text
Offline Replay Dataset
          │
          ▼
YOLOv8m-seg
(FP32 / ONNX / TensorRT)
          │
          ▼
Consistency Analysis
          │
          ▼
Pipeline Profiling
          │
          ▼
Architecture Optimization
          │
          ▼
Performance Benchmarking
```

---

## Key Components

### Model Benchmarking

Benchmarked multiple inference backends using the same replay dataset.

Evaluated:

- PyTorch FP32
- PyTorch FP16
- ONNX Runtime GPU
- TensorRT FP16
- TensorRT INT8

Benchmarking scripts:

```text
benchmarking/
├── yolo_seg_fp16.py
├── yolo_seg_onnx.py
├── yolo_seg_profiling.py
└── yolo_seg_trt.py
```

---

### Model Compression

Implemented model conversion and acceleration workflows.

Completed:

- ONNX export
- TensorRT FP16 engine generation
- TensorRT INT8 engine generation
- INT8 calibration dataset generation

Optimization utilities:

```text
optimization/
├── quantize.py
└── yolo_seg_trt_thread.py
```

---

### Consistency Analysis

Compared TensorRT predictions against the FP32 reference model.

Metrics evaluated:

- Detection Agreement
- Class Agreement
- Bounding Box IoU
- Missed Objects
- Added Objects

Analysis utilities:

```text
consistency_analysis/
├── calibration_images.py
└── consistency_analysis.py
```

---

### Pipeline Profiling

Measured:

- Image preprocessing
- Inference
- Rendering
- Display
- End-to-end pipeline latency

Identified rendering as the dominant bottleneck after inference optimization.

---

### Architecture Optimization

Separated rendering from inference by moving visualization into a dedicated display thread.

Result:

- Rendering and inference executed in parallel.
- TensorRT pipelines achieved substantially higher throughput.

---

## Benchmark Results

### Model Performance

| Model | Avg FPS |
|--------|---------:|
| PyTorch FP32 | 10.16 |
| TensorRT FP16 | 26.33 |
| TensorRT INT8 | 26.81 |

---

### Consistency Analysis

| Metric | TensorRT FP16 | TensorRT INT8 |
|--------|--------------:|--------------:|
| Detection Agreement | 94.75% | 90.23% |
| Class Agreement | 97.77% | 95.41% |
| Mean Box IoU | 0.976 | 0.943 |

---

### Pipeline Profiling

| Component | FP32 | FP16 | INT8 |
|------------|---------:|---------:|---------:|
| Preprocessing | 0.35 ms | 0.37 ms | 0.37 ms |
| Inference | 44.94 ms | 31.55 ms | 24.79 ms |
| Rendering | 14.27 ms | 14.72 ms | 15.90 ms |
| Display | 4.71 ms | 4.67 ms | 4.67 ms |
| Total Pipeline | 64.27 ms | 51.31 ms | 45.91 ms |

---

### End-to-End Performance

| Configuration | Avg FPS |
|---------------|---------:|
| Live CARLA + ROS2 + YOLOv8m-seg | ~3.5 |
| Replay + TensorRT INT8 | ~26 |

Overall throughput improvement:

**~7.4×**

---

## Engineering Findings

- TensorRT significantly reduced inference latency.
- FP16 preserved prediction consistency better than INT8.
- INT8 achieved the highest throughput and lowest CPU utilization.
- ONNX Runtime served as a useful intermediate deployment format.
- Rendering became the dominant bottleneck after inference optimization.
- Threaded rendering enabled pipeline parallelism and significantly increased throughput.
- Pipeline profiling demonstrated that optimizing inference alone is insufficient for maximizing perception performance.

---

## Deliverable

### Model Compression & Pipeline Optimization

**Placeholder for performance comparison GIF/video**

```text
PyTorch FP32
      │
   10.16 FPS
      │
      ▼
TensorRT FP16
      │
   26.33 FPS
      │
      ▼
TensorRT INT8
      │
   26.81 FPS
```

Overall improvement:

**~7.4× higher throughput** compared to the original live CARLA perception pipeline.

---

## Technologies

- ROS2 Humble
- CARLA 0.9.15
- Python
- OpenCV
- YOLOv8m-seg
- ONNX Runtime
- TensorRT
- CUDA
- WSL2 Ubuntu 22.04
- Windows 11

---

## Outcome

Phase 6 completed the optimization cycle for the perception pipeline by combining model compression, prediction consistency analysis, detailed pipeline profiling, and architecture optimization.

The optimized TensorRT perception stack achieved approximately **26 FPS** while maintaining high prediction consistency, establishing a deployment-ready foundation for subsequent multi-modal perception and sensor fusion phases.