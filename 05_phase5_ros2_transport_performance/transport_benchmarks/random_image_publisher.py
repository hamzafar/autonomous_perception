import cv2
import numpy as np
import rclpy

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data

TOPIC_NAME = "/carla/ego_vehicle/rgb_front/image"


class RandomImagePublisher(Node):

    def __init__(self):

        super().__init__("random_image_publisher")

        self.bridge = CvBridge()

        self.publisher = self.create_publisher(
            Image,
            TOPIC_NAME,
            10
        )

        self.counter = 0

        FPS = 3

        self.timer = self.create_timer(
            1.0 / FPS,
            self.publish_image
        )

        # Print statistics once per second
        self.create_timer(
            1.0,
            self.report_rate
        )

        self.get_logger().info(
            "Random image publisher started"
        )

    def publish_image(self):

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

        self.counter += 1

    def report_rate(self):

        self.get_logger().info(
            f"Published images: {self.counter}"
        )


def main():

    rclpy.init()

    node = RandomImagePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
