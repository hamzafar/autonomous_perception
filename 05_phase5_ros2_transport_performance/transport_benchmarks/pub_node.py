import rclpy
from rclpy.node import Node

from example_interfaces.msg import UInt8MultiArray

from std_msgs.msg import Header
import time

class LargeDataPublisher(Node):

    def __init__(self):
        super().__init__('large_data_publisher')

        self.publisher = self.create_publisher(
            UInt8MultiArray,
            '/large_data',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_data)

        self.payload_size_mb = 4

    def publish_data(self):

        msg = UInt8MultiArray()
        msg.data = [123] * (self.payload_size_mb * 1024 * 1024)
        
        
        self.publisher.publish(msg)

        send_time = time.time()

        self.get_logger().info(
            f'Published {self.payload_size_mb} MB'
        )
        self.get_logger().info(
           f"Sent at: {send_time:.3f}"
        )


def main():
    rclpy.init()

    node = LargeDataPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()