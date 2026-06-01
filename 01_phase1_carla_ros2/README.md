# Phase 1 — CARLA + ROS2 Integration

## Objective

Establish a reliable perception pipeline between CARLA Simulator and ROS2, enabling real-time sensor data streaming and visualization within a Linux-based robotics development environment.

This phase focused on validating end-to-end communication across:

CARLA → ROS Bridge → ROS2 Topics → OpenCV Visualization

---

## Architecture

```text
CARLA Simulator (Windows 11)
        │
        ▼
CARLA ROS Bridge
        │
        ▼
ROS2 Humble (WSL2 Ubuntu 22.04)
        │
        ▼
RGB Camera Topic
        │
        ▼
OpenCV Visualization
```

---

## Key Components

### Environment Setup

Scripts used to configure the ROS2 environment, DDS communication settings, and CARLA integration.

**Files**

- `scripts/source_ros.sh`
- `scripts/start_carla_bridge.sh`

---

### Sensor Configuration

CARLA sensor definition used to spawn the ego vehicle and front-facing RGB camera.

**File**

- `config/ego_rgb.json`

Configuration includes:

- Tesla Model 3 ego vehicle
- Autopilot enabled
- Front RGB camera
- Resolution: 800×600
- Field of View: 90°

---

### Validation Application

ROS2 subscriber node responsible for receiving RGB images and displaying them through OpenCV.

**File**

- `code/view_camera.py`

Responsibilities:

- Subscribe to CARLA RGB camera topic
- Convert ROS Image messages using CvBridge
- Display real-time video stream
- Validate end-to-end data flow

---

## Validation Results

Successfully validated:

- Windows ↔ WSL2 networking
- CARLA ↔ ROS2 communication
- DDS-based discovery and messaging
- CARLA ROS Bridge integration
- RGB camera streaming
- ROS2 image transport
- OpenCV visualization
- End-to-end perception data flow

---

## Deliverables

### Real-Time RGB Camera Streaming

<p align="center">
  <img src="../assets/gifs/phase1_pipeline.gif" width="700"/>
</p>

<p align="center">
  End-to-end CARLA → ROS2 → OpenCV perception pipeline validation.
</p>

---

## Technologies

- CARLA 0.9.15
- ROS2 Humble
- Python
- OpenCV
- CvBridge
- CycloneDDS
- WSL2 Ubuntu 22.04
- Windows 11

---
## Engineering Challenges

### CARLA ↔ ROS2 Communication

**Challenge**

ROS2 running inside WSL2 could not communicate reliably with the CARLA simulator running on Windows.

**Resolution**

- Verified network connectivity from WSL2
- Validated CARLA accessibility from Windows
- Confirmed ROS2 environment configuration
- Isolated the issue to WSL2 ↔ Windows communication
- Implemented WSL2 mirrored networking

**Outcome**

Reliable CARLA ↔ ROS2 communication was established for real-time sensor streaming.

---
## Outcome

Phase 1 established the foundational communication layer required for subsequent perception development. The validated pipeline provided the basis for integrating real-time object detection, modular ROS2 architectures, profiling workflows, and future autonomous perception capabilities.