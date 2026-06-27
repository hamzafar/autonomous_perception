import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

import cv2
import time
import torch

import os
import threading

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


        self.bridge = CvBridge()

        # ==========================
        # Display Thread
        # ==========================
        self.latest_frame = None
        self.latest_results = None

        self.display_lock = threading.Lock()

        self.running = True

        self.display_thread = threading.Thread(
            target=self.display_loop,
            daemon=True
        )

        self.display_thread.start()

        # # Force CPU
        # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

        # Yolo Segmentation  model
        self.model = YOLO(TRT_INT8)

        self.get_logger().info(
            f"Loaded model: {self.model.ckpt_path}"
        )

        self.get_logger().info(
            "YOLOv8m-seg TRT model loaded"
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

        # ROS Image -> OpenCV
        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding="bgr8"
        )

        # YOLO inference
        results = self.model(
            frame,
            imgsz=640,
            verbose=False
        )

        with self.display_lock:
            self.latest_results = results

        # Draw segmentation masks, boxes, labels
        #annotated_frame = results[0].plot()

        # ==========================
        # FPS Calculation
        # ==========================
        self.frame_count += 1

        elapsed = time.time() - self.start_time

        if elapsed >= 1.0:
            self.fps = self.frame_count / elapsed

            self.fps_history.append(self.fps)

            self.frame_count = 0

            # Avoid drift
            self.start_time += elapsed


        # ==========================
        # FPS MIN, MAX, AVG
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

            self.fps_history.clear()

            self.benchmark_start = time.time() 

        # ==========================
        # Draw FPS
        # ==========================
        # if self.show_fps:
        #     cv2.putText(
        #         annotated_frame,
        #         f"FPS: {self.fps:.1f}",
        #         (20, 40),
        #         cv2.FONT_HERSHEY_SIMPLEX,
        #         1,
        #         (0, 255, 0),
        #         2
        #     )

        # # ==========================
        # # Display
        # # ==========================
        # cv2.imshow(
        #     "YOLOv8 Segmentation",
        #     annotated_frame
        # )

        # cv2.waitKey(1)

        # ==========================
        # Send frame to display thread
        # ==========================
        # with self.display_lock:

        #     self.latest_frame = annotated_frame
        

    def display_loop(self):

        while self.running:

            results = None

            with self.display_lock:

                if self.latest_results is not None:

                    results = self.latest_results

            if results is not None:

                annotated_frame = results[0].plot()

                cv2.putText(
                    annotated_frame,
                    # f"FPS: {self.fps:.1f}",
                    f"Sim To Real",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                cv2.imshow(
                    "YOLOv8 Segmentation",
                    annotated_frame
                )

                cv2.waitKey(1)

            else:

                time.sleep(0.01)
                

    # def display_loop(self):
        
    #     while self.running:

    #         frame = None

    #         with self.display_lock:

    #             if self.latest_frame is not None:

    #                 frame = self.latest_frame.copy()

    #         if frame is not None:

    #             cv2.imshow(
    #                 "YOLOv8 Segmentation",
    #                 frame
    #             )

    #             cv2.waitKey(1)

    #         else:

    #             time.sleep(0.01)


def main(args=None):

    rclpy.init(args=args)

    node = YoloSegDetector()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.running = False

    node.display_thread.join(timeout=1)

    node.destroy_node()

    rclpy.shutdown()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()