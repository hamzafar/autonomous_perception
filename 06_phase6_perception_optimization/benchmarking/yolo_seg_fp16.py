import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

import cv2
import time
import torch


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
        

        self.bridge = CvBridge()

        # Segmentation model
        self.model = YOLO("yolov8m-seg.pt")

        # Move model to GPU
        if not torch.cuda.is_available():
            raise RuntimeError(
                "FP16 requires CUDA GPU"
            )
        self.model.to("cuda")

        # Convert model weights to FP16
        self.model.model.half()

        self.get_logger().info(
            "YOLOv8m-seg FP16 model loaded"
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

        # Draw segmentation masks, boxes, labels
        annotated_frame = results[0].plot()

        # ==========================
        # FPS Calculation
        # ==========================
        self.frame_count += 1

        elapsed = time.time() - self.start_time

        if elapsed >= 1.0:
            self.fps = self.frame_count / elapsed

            self.frame_count = 0

            # Avoid drift
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
        # Display
        # ==========================
        cv2.imshow(
            "YOLOv8 Segmentation",
            annotated_frame
        )

        cv2.waitKey(1)


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