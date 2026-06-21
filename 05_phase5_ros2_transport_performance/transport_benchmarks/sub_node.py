import rclpy
from rclpy.node import Node
from example_interfaces.msg import UInt8MultiArray
import time



class LargeDataSubscriber(Node):

    def __init__(self):
        super().__init__('large_data_subscriber')

        self.count = 0
        self.total_bytes = 0

        self.subscription = self.create_subscription(
            UInt8MultiArray,
            '/large_data',
            self.callback,
            10
        )

    def callback(self, msg):

        self.count += 1
        self.total_bytes += len(msg.data)

        self.get_logger().info(
            f"Received #{self.count} | "
            f"Size={len(msg.data)/(1024*1024):.2f} MB"
        )
        receive_time = time.time()

        self.get_logger().info(
           f"Received at: {receive_time:.3f}"
        )


def main():
    rclpy.init()
    node = LargeDataSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()