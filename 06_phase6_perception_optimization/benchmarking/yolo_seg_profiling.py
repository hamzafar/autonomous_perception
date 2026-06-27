import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

import cv2
import time
import torch

import os

# /home/hamza/ros2_cv_ws/scripts/phase6/engines/yolov8m-seg-trt-fp16.engine
TRT_INT8 = "/home/hamza/ros2_cv_ws/scripts/phase6/engines/yolov8m-seg-trt-int8.engine"
TRT_FP16 = "/home/hamza/ros2_cv_ws/scripts/phase6/engines/yolov8m-seg-trt-fp16.engine"
PYT_FP32 = "/home/hamza/ros2_cv_ws/scripts/phase6/test/yolov8m-seg.pt"

class YoloSegDetector(Node):

    def __init__(self):

        super().__init__('yolo_seg_detector')

        # ==========================
        # User Settings
        # ==========================
        self.show_fps = True

        # FPS counters
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0.0
        
        # =======================
        # FPS calculatoin
        # ========================
        self.fps_history = []

        self.benchmark_start = time.time()
        self.benchmark_duration = 60

        # =======================
        # Profiling
        # =======================
        self.profile_preprocess = []
        self.profile_inference = []
        self.profile_render = []
        self.profile_display = []
        self.profile_total = []

        self.profile_warmup = 10

        self.bridge = CvBridge()

        # # Force CPU
        # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

        # Yolo Segmentation  model
        self.model = YOLO(PYT_FP32)


        self.get_logger().info(
            "YOLOv8m-seg model loaded"
        )

        self.get_logger().info(
            f"Loaded model: {self.model.ckpt_path}"
        )

        self.subscription = self.create_subscription(
            Image,
            "/carla/ego_vehicle/rgb_front/image",
            self.image_callback,
            10
        )

        self.get_logger().info(
            "YOLOv8 Segmentation node started"
        )

    def image_callback(self, msg):

        callback_start = time.perf_counter()

        # ==========================
        # Image Preprocessing
        # ==========================
        t0 = time.perf_counter()

        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding="bgr8"
        )

        preprocess_ms = (
            time.perf_counter() - t0
        ) * 1000

        # ==========================
        # YOLO Inference
        # ==========================
        t0 = time.perf_counter()

        results = self.model(
            frame,
            imgsz=640,
            verbose=False
        )

        inference_ms = (
            time.perf_counter() - t0
        ) * 1000

        # ==========================
        # Rendering
        # ==========================
        t0 = time.perf_counter()

        annotated_frame = results[0].plot()

        render_ms = (
            time.perf_counter() - t0
        ) * 1000

        # ==========================
        # FPS Calculation
        # ==========================
        self.frame_count += 1

        elapsed = time.time() - self.start_time

        if elapsed >= 1.0:

            self.fps = self.frame_count / elapsed

            self.fps_history.append(self.fps)

            self.frame_count = 0

            self.start_time += elapsed

        # ==========================
        # Draw FPS
        # ==========================
        if self.show_fps:
            cv2.putText(
                annotated_frame,
                f"FPS: {self.fps:.1f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # ==========================
        # OpenCV Display
        # ==========================
        t0 = time.perf_counter()

        cv2.imshow(
            "YOLOv8 Segmentation",
            annotated_frame
        )

        cv2.waitKey(1)

        display_ms = (
            time.perf_counter() - t0
        ) * 1000

        # ==========================
        # Total Pipeline
        # ==========================
        total_ms = (
            time.perf_counter() - callback_start
        ) * 1000

        # ==========================
        # Profiling Collection
        # ==========================
        runtime = (
            time.time() -
            self.benchmark_start
        )

        if runtime > self.profile_warmup:

            self.profile_preprocess.append(
                preprocess_ms
            )

            self.profile_inference.append(
                inference_ms
            )

            self.profile_render.append(
                render_ms
            )

            self.profile_display.append(
                display_ms
            )

            self.profile_total.append(
                total_ms
            )

        # ==========================
        # FPS Benchmark
        # ==========================
        if (
            time.time() - self.benchmark_start
            >= self.benchmark_duration
            and len(self.fps_history) > 0
        ):

            min_fps = min(self.fps_history)

            max_fps = max(self.fps_history)

            avg_fps = (
                sum(self.fps_history)
                / len(self.fps_history)
            )

            self.get_logger().info(
                f"60s Benchmark | "
                f"Samples: {len(self.fps_history)} | "
                f"Min FPS: {min_fps:.2f} | "
                f"Avg FPS: {avg_fps:.2f} | "
                f"Max FPS: {max_fps:.2f}"
            )

            # ==========================
            # Profiling Report
            # ==========================
            self.get_logger().info(
                "===== Pipeline Profiling ====="
            )

            self.get_logger().info(
                f"Preprocessing : "
                f"{sum(self.profile_preprocess)/len(self.profile_preprocess):.2f} ms"
            )

            self.get_logger().info(
                f"Inference     : "
                f"{sum(self.profile_inference)/len(self.profile_inference):.2f} ms"
            )

            self.get_logger().info(
                f"Rendering     : "
                f"{sum(self.profile_render)/len(self.profile_render):.2f} ms"
            )

            self.get_logger().info(
                f"Display       : "
                f"{sum(self.profile_display)/len(self.profile_display):.2f} ms"
            )

            self.get_logger().info(
                f"Total Pipeline: "
                f"{sum(self.profile_total)/len(self.profile_total):.2f} ms"
            )

            self.fps_history.clear()

            self.profile_preprocess.clear()
            self.profile_inference.clear()
            self.profile_render.clear()
            self.profile_display.clear()
            self.profile_total.clear()

            self.benchmark_start = time.time()

def main(args=None):

    rclpy.init(args=args)

    node = YoloSegDetector()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()