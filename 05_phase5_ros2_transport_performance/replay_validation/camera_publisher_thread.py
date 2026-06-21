import os
import glob
import cv2
import time
import threading

import rclpy

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from rclpy.qos import qos_profile_sensor_data


# ==================================================
# CONFIGURATION
# ==================================================

SESSION_DIR = "/home/hamza/ros2_cv_ws/scripts/phase4/recordings/session_20260530_204754"

THREAD_FPS = 3

NUM_THREADS = 3

TOPIC_NAME = "/carla/ego_vehicle/rgb_front/image"

# ==================================================


class CameraPublisher(Node):

    def __init__(self):

        super().__init__("camera_publisher")

        self.bridge = CvBridge()

        self.publisher = self.create_publisher(
            Image,
            TOPIC_NAME,
            10
        )

        self.image_files = sorted(
            glob.glob(
                os.path.join(
                    SESSION_DIR,
                    "*.jpg"
                )
            )
        )

        if len(self.image_files) == 0:

            self.get_logger().error(
                f"No images found in {SESSION_DIR}"
            )

            raise RuntimeError(
                "Dataset is empty"
            )

        self.total_frames = len(
            self.image_files
        )

        self.current_index = 0

        self.published_frames = 0

        self.index_lock = threading.Lock()

        self.counter_lock = threading.Lock()

        self.get_logger().info(
            f"Loaded {self.total_frames} images"
        )

        self.get_logger().info(
            f"Starting {NUM_THREADS} threads "
            f"at {THREAD_FPS} FPS each"
        )

        for _ in range(NUM_THREADS):

            thread = threading.Thread(
                target=self.publish_loop,
                daemon=True
            )

            thread.start()

        self.create_timer(
            1.0,
            self.report_rate
        )

    def get_next_index(self):

        with self.index_lock:

            index = self.current_index

            self.current_index += 1

            if self.current_index >= self.total_frames:

                self.get_logger().info("")
                self.get_logger().info(
                    "===== Replay Summary ====="
                )

                self.get_logger().info(
                    f"Published Frames: "
                    f"{self.published_frames}"
                )

                self.get_logger().info(
                    "Restarting dataset..."
                )

                self.current_index = 0

                self.published_frames = 0

            return index

    def publish_loop(self):

        period = 1.0 / THREAD_FPS

        while rclpy.ok():

            frame_index = (
                self.get_next_index()
            )

            image_path = self.image_files[
                frame_index
            ]

            image = cv2.imread(
                image_path
            )

            if image is None:

                self.get_logger().warning(
                    f"Failed to load: "
                    f"{image_path}"
                )

                continue

            ros_msg = self.bridge.cv2_to_imgmsg(
                image,
                encoding="bgr8"
            )

            ros_msg.header.stamp = (
                self.get_clock()
                .now()
                .to_msg()
            )

            ros_msg.header.frame_id = (
                "rgb_front"
            )

            self.publisher.publish(
                ros_msg
            )

            with self.counter_lock:

                self.published_frames += 1

            time.sleep(
                period
            )

    def report_rate(self):

        self.get_logger().info(
            f"Published Frames: "
            f"{self.published_frames}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = CameraPublisher()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        node.get_logger().info(
            "Shutting down..."
        )

    finally:

        node.destroy_node()

        rclpy.shutdown()


if __name__ == "__main__":

    main()
