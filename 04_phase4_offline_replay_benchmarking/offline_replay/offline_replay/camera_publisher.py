import os
import glob
import cv2
import rclpy

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from rclpy.qos import qos_profile_sensor_data


# ==================================================
# CONFIGURATION
# ==================================================

# SESSION_DIR = "recordings/session_20260530_204754"

# REPLAY_FPS = 4

# TOPIC_NAME = "/carla/ego_vehicle/rgb_front/image"

# ==================================================


class CameraPublisher(Node):

    def __init__(self):

        super().__init__("camera_publisher")

        self.bridge = CvBridge()
 
        self.declare_parameter(
            'session_dir',
            '/home/hamza/ros2_cv_ws/scripts/phase4/recordings/session_20260530_204754'
        )

        self.declare_parameter(
            'replay_fps',
            4
        )

        self.declare_parameter(
            'topic_name',
            '/carla/ego_vehicle/rgb_front/image'
        )


        self.session_dir = self.get_parameter(
            'session_dir'
        ).value

        self.replay_fps = self.get_parameter(
            'replay_fps'
        ).value

        self.topic_name = self.get_parameter(
            'topic_name'
        ).value

        self.publisher = self.create_publisher(
            Image,
            self.topic_name,
            10
        )

        self.image_files = sorted(
            glob.glob(
                os.path.join(
                    self.session_dir,
                    "*.jpg"
                )
            )
        )

        if len(self.image_files) == 0:

            self.get_logger().error(
                f"No images found in {self.session_dir}"
            )

            raise RuntimeError(
                "Dataset is empty"
            )

        self.total_frames = len(
            self.image_files
        )

        self.current_index = 0

        self.published_frames = 0

        # self.replay_completed = False

        self.get_logger().info(
            f"Loaded {self.total_frames} images"
        )

        timer_period = 1.0 / self.replay_fps

        self.timer = self.create_timer(
            timer_period,
            self.publish_next_frame
        )

        self.get_logger().info(
            f"Publishing at {self.replay_fps} FPS"
        )

    def publish_next_frame(self):

        
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

            return
        

        
        if self.current_index == 0:

            self.get_logger().info(
                "Starting new iteration"
            )

     
        image_path = self.image_files[
            self.current_index
        ]

        image = cv2.imread(
            image_path
        )

        if image is None:

            self.get_logger().warning(
                f"Failed to load: "
                f"{image_path}"
            )

            self.current_index += 1

            return

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

        self.current_index += 1

        self.published_frames += 1

        if (
            self.published_frames % 100
            == 0
        ):

            self.get_logger().info(
                f"Published="
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