# Phase 5 — ROS2 Transport Performance Investigation

## Objective

Investigate ROS2 image transport performance, DDS behavior, throughput limitations, latency, and scalability using both synthetic image streams and recorded CARLA datasets.

This phase focused on understanding transport bottlenecks, evaluating DDS scalability, benchmarking ROS2 image streaming performance, and validating perception workloads over ROS2 communication channels.

---

## Architecture

```text
Offline Dataset
        │
        ▼
Replay Publisher
        │
        ▼
DDS Transport
        │
        ▼
ROS2 Subscriber
        │
        ├────────────► OpenCV Viewer
        │
        └────────────► YOLOv8m-seg
```

---

## Key Components

### DDS Transport Investigation

Validated large-message transport using CycloneDDS.

Payloads tested:

- 16 MB
- 32 MB
- 64 MB

Findings:

- DDS successfully transported all payload sizes.
- Larger payloads increased latency.
- DDS remained stable throughout testing.

---

### Throughput Benchmarking

Developed benchmarking nodes to evaluate publisher and subscriber performance.

Investigated:

- Publisher throughput
- Subscriber throughput
- Aggregate throughput
- Image transport stability
- Message delivery behavior

Benchmarking utilities:

```text
transport_benchmarks/
├── pub_node.py
├── sub_node.py
├── random_image_publisher.py
└── random_image_publisher_thread.py
```

---

### QoS Investigation

Evaluated ROS2 transport behavior under different QoS settings.

Explored:

- sensor_data QoS
- Queue depth tuning
- Latest-frame delivery behavior
- Subscriber backlog effects

---

### Multi-Threaded Publisher Investigation

Implemented a shared-frame multi-threaded publishing architecture.

Validated configurations:

- 3 threads × 3 FPS
- 4 threads × 3 FPS
- 5 threads × 3 FPS

Findings:

- Throughput scaled approximately linearly.
- DDS remained stable.
- Viewer remained stable.
- YOLO inference remained stable.

---

### Replay Validation

Validated end-to-end transport using recorded CARLA datasets.

Validated pipelines:

```text
Dataset
    │
    ▼
Replay Publisher
    │
    ▼
DDS
    │
    ▼
OpenCV Viewer
```

```text
Dataset
    │
    ▼
Replay Publisher
    │
    ▼
DDS
    │
    ▼
YOLOv8m-seg
```

Validation utilities:

```text
replay_validation/
├── camera_publisher_thread.py
├── only_image_subscriber.py
├── show_image_subscriber.py
└── yolo_seg.py
```

---

## Benchmark Results

### Throughput Comparison

| Configuration | Throughput |
|---------------|-----------:|
| Live CARLA Publisher | ~3 FPS |
| Offline Replay Publisher | ~8 FPS |
| Multi-Thread DDS Publisher | ~15 FPS |

### Multi-Publisher Scaling

| Configuration | Aggregate Throughput |
|---------------|--------------------:|
| 7 Publishers × 3 FPS | >20 FPS |

---

## Engineering Findings

- DDS successfully handles large payload transport.
- Large payloads increase latency but remain functional.
- CPU is not the primary bottleneck.
- Aggregate throughput scales beyond 20 FPS.
- Multiple low-rate publishers outperform a single high-rate publisher.
- Publisher-side multithreading significantly improves throughput.
- ROS2 image transport is suitable for perception workloads.
- Offline replay provides deterministic benchmarking.
- End-to-end replay → ROS2 → YOLOv8m-seg pipeline remains stable.
- Transport limitations appear related to queueing and buffering rather than DDS bandwidth.

---

## Deliverable

### ROS2 Image Transport Optimization

**Placeholder for throughput comparison GIF/video**

```text
Live CARLA Publisher
        ↓
      ~3 FPS

Offline Replay Publisher
        ↓
      ~8 FPS

Multi-Thread DDS Publisher
        ↓
     ~15 FPS
```

Overall throughput improvement:

**~5× increase**

from live CARLA publishing to multi-threaded DDS publishing.

---

## Technologies

- ROS2 Humble
- CycloneDDS
- Python
- OpenCV
- YOLOv8m-seg
- CARLA 0.9.15
- WSL2 Ubuntu 22.04
- Windows 11

---

## Outcome

Phase 5 validated the performance characteristics of ROS2 image transport for robotics perception workloads.

The investigation demonstrated that DDS transport remained reliable under large payloads, throughput scaled through publisher-side parallelism, and replay-based benchmarking provided a deterministic environment for transport analysis and perception evaluation.