import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

import cv2


class YoloDetector(Node):

    def __init__(self):

        super().__init__('yolo_detector')
        self.bridge = CvBridge()
        
        self.declare_parameter(
            'model_path',
            '/home/hamza/ros2_cv_ws/models/yolov8n.pt'
            )

        model_path = self.get_parameter(
            'model_path'
            ).value

        
        self.model = YOLO(model_path)

        self.subscription = self.create_subscription(
            Image,
            '/carla/ego_vehicle/rgb_front/image',
            self.image_callback,
            10
        )

        self.get_logger().info("YOLO detector started")


    def image_callback(self, msg):

        # ROS image -> OpenCV
        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='bgr8'
        )

        # YOLO inference
        results = self.model(frame)

        # Draw detections
        annotated_frame = results[0].plot()

        # Visualization
        cv2.imshow("YOLO Detection", annotated_frame)

        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = YoloDetector()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()