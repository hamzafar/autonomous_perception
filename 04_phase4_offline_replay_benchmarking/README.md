# Phase 4 — Offline Replay & Benchmarking

## Objective

Develop a benchmarking and evaluation framework for robotics perception workloads by separating perception algorithms from simulator execution.

This phase focused on profiling hardware utilization, generating deterministic datasets, building an offline replay pipeline, and validating perception performance without requiring a live CARLA simulation.

---

## Architecture

```text
Online Pipeline

CARLA Simulator
        │
        ▼
ROS Bridge
        │
        ▼
ROS2 Image Topic
        │
        ▼
Viewer / YOLO


Offline Pipeline

Recorded Dataset
        │
        ▼
Offline Replay Publisher
        │
        ▼
ROS2 Image Topic
        │
        ▼
Viewer / YOLO
```

---

## Key Components

### Hardware Profiling

Resource utilization analysis was performed across multiple perception workloads to understand the computational cost of simulation, ROS communication, visualization, and inference.

Evaluated metrics:

- CPU utilization
- RAM consumption
- GPU utilization
- VRAM consumption

Workloads profiled:

- CARLA only
- CARLA + ROS Bridge
- CARLA + Viewer
- CARLA + YOLO

---

### Dataset Recording

A dataset generation pipeline was developed to capture RGB camera streams directly from CARLA.

Capabilities:

- Timestamped dataset generation
- Fixed-frame recording
- Fixed-duration recording
- Queue-based asynchronous recording
- Deterministic synchronous recording

Key validation results:

- 100/100 synchronized captures
- 900/900 synchronized captures
- Zero-frame-loss recording
- Tick-to-image synchronization validation

---

### Offline Replay Infrastructure

A ROS2 package was developed to replay recorded datasets as live ROS image topics.

**ROS2 Package**

```text
offline_replay
```

Capabilities:

- Replay recorded datasets
- Publish ROS2 image streams
- Configurable replay FPS
- Launch-based deployment
- Replay without CARLA

---

### Replay-Based Perception Evaluation

The replay pipeline enabled perception workloads to be evaluated independently of simulator execution.

Validated pipelines:

```text
Dataset
    │
    ▼
Replay Publisher
    │
    ▼
ROS2 Image Topic
    │
    ├────────────► Viewer
    │
    └────────────► YOLO
```

This allowed repeatable benchmarking and deterministic perception testing.

---

### Dataset Utilities

Supporting tools were developed for dataset preparation and experimentation.

Capabilities:

- Multi-resolution dataset generation
- Dataset resizing
- Replay visualization
- Dataset inspection

---

## Benchmark Results

### Online Profiling

| Scenario | CPU | RAM | GPU |
|-----------|------|------|------|
| CARLA Only | 48% | ~8 GB | 38% |
| CARLA + ROS Bridge | 65% | ~9 GB | 40% |
| CARLA + Viewer | 70% | ~11 GB | 40% |
| CARLA + YOLO | 75% | ~13.5 GB | 60% |

---

### Offline Replay Profiling

| Scenario | CPU | RAM | GPU |
|-----------|------|------|------|
| Replay Publisher + Viewer | ~30% | ~8 GB | N/A |
| Replay Publisher + YOLO | ~30% | ~9.5 GB | ~30% |

---

## Engineering Challenges

### Deterministic Dataset Generation

#### Challenge

Perception benchmarking requires repeatable input data. Traditional recording methods can introduce timing inconsistencies, dropped frames, and synchronization issues between simulation ticks and captured images.

#### Resolution

- Implemented synchronous CARLA execution
- Fixed simulator timestep
- Validated tick-to-image synchronization
- Verified capture consistency across large recording sessions

#### Outcome

Achieved deterministic dataset generation with zero-frame-loss validation across both 100-frame and 900-frame recording sessions.

---

## Deliverables

### Online vs Offline Perception Comparison

<p align="center">
  <img src="../assets/gifs/phase4_pipeline.gif" width="700"/>
</p>

<p align="center">
  This comparison demonstrates the resource utilization differences between simulator-based perception and replay-based perception evaluation.
</p>

---

## Technologies

- CARLA 0.9.15
- ROS2 Humble
- Python
- OpenCV
- YOLOv8
- CvBridge
- CycloneDDS
- WSL2 Ubuntu 22.04
- Windows 11

---

## Outcome

Phase 4 established a reusable benchmarking and evaluation framework for robotics perception development.

The resulting infrastructure enabled deterministic dataset generation, offline replay, repeatable perception experiments, and resource utilization analysis. This framework became the foundation for subsequent transport benchmarking and perception optimization phases.