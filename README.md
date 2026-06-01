# Autonomous Perception

A robotics perception engineering project documenting the transition from traditional 2D computer vision to ROS2-based autonomous perception systems.

Built using CARLA, ROS2, OpenCV, and YOLOv8, the project progresses through a series of engineering phases covering simulator integration, perception pipelines, modular ROS2 architectures, and system validation workflows.


---

## Technology Stack

| Category | Technologies |
|-----------|-------------|
| Simulation | CARLA 0.9.15 |
| Robotics Middleware | ROS2 Humble |
| Computer Vision | OpenCV |
| Object Detection | YOLOv8 |
| Programming Language | Python |
| Communication | CycloneDDS |
| Environment | Windows 11 + WSL2 Ubuntu 22.04 |

---

## System Architecture

```text
CARLA Simulator
        │
        ▼
ROS2 Communication Layer
        │
        ▼
Perception Pipeline
        │
        ▼
Modular ROS2 Architecture
        │
        ▼
Validation & Benchmarking
```

---

## Completed Phases

### ✅ Phase 1 — CARLA + ROS2 Integration

Validated end-to-end communication between CARLA and ROS2 using RGB camera streaming and OpenCV visualization.

📁 [View Phase 1](01_phase1_carla_ros2)

---

### ✅ Phase 2 — Real-Time Object Detection

Integrated YOLOv8 into the ROS2 perception pipeline for real-time object detection and visualization.

📁 [View Phase 2](02_phase2_yolo_detection)

---

### ✅ Phase 3 — Modular ROS2 Architecture

Converted standalone scripts into a reusable ROS2 package architecture with launch files, configuration management, and automated deployment workflows.

📁 [View Phase 3](03_phase3_ros2_architecture)

---

### 🚧 Phase 4 — Offline Replay & Benchmarking

Documentation will be published after project milestone release.

📁 [View Phase 4](04_phase4_offline_replay_benchmarking)

---

## Demonstrations

| Phase 1 — CARLA + ROS2 Integration | Phase 2 — Real-Time Object Detection |
|------------------------------------|--------------------------------------|
| <img src="assets/gifs/phase1_pipeline.gif" width="350" height="200"/> | <img src="assets/gifs/phase2_pipeline.gif" width="350" height="200"/> |
| End-to-end CARLA → ROS2 → OpenCV pipeline validation | Real-time object detection using YOLOv8 and ROS2 |
---


## Future Work

Planned areas of development include:

- Network profiling and communication analysis
- Sensor synchronization
- Multi-camera perception
- 3D perception workflows
- Sensor fusion
- Autonomous systems engineering workflows

---

## Project Journal

Detailed development notes, planning, experiments, and progress tracking are maintained separately:

- `roadmap/project_journal.md`