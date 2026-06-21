import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from rclpy.qos import qos_profile_sensor_data


TOPIC_NAME = "/carla/ego_vehicle/rgb_front/image"


class ImageSubscriber(Node):

    def __init__(self):

        super().__init__("image_subscriber")

        self.counter = 0

        self.subscription = self.create_subscription(
            Image,
            TOPIC_NAME,
            self.image_callback,
            10
        )

        self.create_timer(
            1.0,
            self.report_rate
        )

        self.get_logger().info(
            "Image subscriber started"
        )

    def image_callback(self, msg):

        self.counter += 1

    def report_rate(self):

        self.get_logger().info(
            f"Received images: {self.counter}"
        )


def main():

    rclpy.init()

    node = ImageSubscriber()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
