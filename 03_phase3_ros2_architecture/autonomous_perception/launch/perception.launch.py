from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='autonomous_perception',
            executable='view_camera',
            name='view_camera'
        ),

        Node(
            package='autonomous_perception',
            executable='yolo_detector',
            name='yolo_detector'
        )

    ])