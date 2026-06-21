import threading
import time

import numpy as np
import rclpy

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from rclpy.qos import QoSProfile




TOPIC_NAME = "/carla/ego_vehicle/rgb_front/image"

FPS = 3
NUM_THREADS = 3


class MultiThreadPublisher(Node):

    def __init__(self):

        super().__init__("multi_thread_publisher")

        self.bridge = CvBridge()

        self.counter = 0

        self.counter_lock = threading.Lock()

        self.publisher = self.create_publisher(
            Image,
            TOPIC_NAME,
            10
        )

        for i in range(NUM_THREADS):

            thread = threading.Thread(
                target=self.publish_loop,
                daemon=True
            )

            thread.start()

        self.create_timer(
            1.0,
            self.report_rate
        )

        self.get_logger().info(
            f"Started {NUM_THREADS} publisher threads "
            f"on topic: {TOPIC_NAME}"
        )

    def publish_loop(self):

        period = 1.0 / FPS

        while rclpy.ok():

            image = np.random.randint(
                0,
                256,
                (480, 640, 3),
                dtype=np.uint8
            )

            ros_msg = self.bridge.cv2_to_imgmsg(
                image,
                encoding="bgr8"
            )

            self.publisher.publish(
                ros_msg
            )

            with self.counter_lock:
                self.counter += 1

            time.sleep(
                period
            )

    def report_rate(self):

        self.get_logger().info(
            f"Published images: {self.counter}"
        )


def main():

    rclpy.init()

    node = MultiThreadPublisher()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()