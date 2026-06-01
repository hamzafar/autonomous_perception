import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2

import time


class CameraViewer(Node):

    def __init__(self):
        super().__init__('camera_viewer')

        #### debugging
        self.counter = 0
        self.frame_count = 0
        self.start_time = time.time()

        self.bridge = CvBridge()

        self.declare_parameter(
            'car_camera',
            '/carla/ego_vehicle/rgb_front/image'
            )

        car_camera = self.get_parameter(
            'car_camera'
            ).value

        self.subscription = self.create_subscription(
            Image,
            car_camera,
            self.image_callback,
            10
        )

        #### debug
        # self.timer = self.create_timer(
        #     3.0,
        #     self.report
        #     )

        self.get_logger().info("Camera viewer node started.")

    def image_callback_debug(self, msg):

        self.counter += 1

    def report(self):

        print(f"Received: {self.counter}")


    def image_callback(self, msg):
        
        #### debugging only
        # self.counter += 1
        # print(f"Received image {self.counter}")
        # self.frame_count += 1

        elapsed = time.time() - self.start_time
        fps = self.frame_count / elapsed
        

        # ROS Image -> OpenCV image
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')


        #### debug
        # cv2.putText(
        #     frame,
        #     f"FPS: {fps:.2f}",
        #     (10, 30),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     1,
        #     (0, 255, 0),
        #     2
        #     )

        # Show image
        cv2.imshow("CARLA RGB Camera", frame)

        # Required for OpenCV GUI refresh
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = CameraViewer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
