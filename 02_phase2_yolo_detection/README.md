# Phase 2 — Real-Time Object Detection

## Objective

Extend the perception pipeline established in Phase 1 by integrating a deep learning-based object detector capable of performing real-time inference on camera data streamed from CARLA through ROS2.

This phase focused on validating the complete perception workflow:

CARLA → ROS2 → YOLOv8 → Detection Visualization

---

## Architecture

```text
CARLA Simulator (Windows 11)
        │
        ▼
RGB Camera Sensor
        │
        ▼
CARLA ROS Bridge
        │
        ▼
ROS2 Image Topic
        │
        ▼
YOLOv8 Detector
        │
        ▼
Annotated Detection Output
```

---

## Key Components

### Object Detection Node

ROS2 node responsible for subscribing to the RGB camera stream, performing YOLOv8 inference, and visualizing detection results.

**File**

- `code/yolo_detector.py`

Responsibilities:

- Subscribe to CARLA RGB image topic
- Convert ROS Image messages using CvBridge
- Perform YOLOv8 inference
- Render bounding boxes and class labels
- Display annotated detections in real time

---

## Validation Results

Successfully validated:

- Real-time image streaming from CARLA
- ROS2 image subscription pipeline
- YOLOv8 integration
- Real-time object detection
- Detection visualization
- Dynamic scene perception
- End-to-end perception workflow

---

## Deliverables

### Real-Time Object Detection

<p align="center">
  <img src="../assets/gifs/phase2_pipeline.gif" width="700"/>
</p>

<p align="center">
  Real-time object detection on CARLA driving scenes using YOLOv8 and ROS2.
</p>

---

## Engineering Challenges

### Ego Vehicle Autopilot Configuration

#### Challenge

The ego vehicle was successfully spawned in CARLA, but autonomous driving behavior was not functioning correctly. Instead of navigating naturally through the environment, the vehicle appeared to change position without continuous motion.

#### Resolution

- Investigated vehicle spawning and sensor configuration
- Explicitly defined the ego vehicle using a JSON object configuration
- Configured a fixed spawn point and camera placement
- Validated autopilot behavior after configuration updates

#### Outcome

The ego vehicle successfully navigated the CARLA environment using autopilot, enabling realistic perception testing and continuous object detection on dynamic driving scenes.

---

## Technologies

- CARLA 0.9.15
- ROS2 Humble
- Python
- OpenCV
- YOLOv8
- Ultralytics
- CvBridge
- CycloneDDS
- WSL2 Ubuntu 22.04
- Windows 11

---

## Outcome

Phase 2 transformed the project from a sensor streaming pipeline into a functional perception system. Real-time object detection was successfully integrated into the ROS2 workflow, providing the foundation for modular perception architectures, benchmarking, and future autonomous driving capabilities.