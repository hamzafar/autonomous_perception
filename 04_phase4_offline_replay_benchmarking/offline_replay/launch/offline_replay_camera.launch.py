from launch import LaunchDescription

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
import os



def generate_launch_description():

    replay_config = os.path.join(
    get_package_share_directory('offline_replay'),
    'config',
    'replay.yaml'
    )

    return LaunchDescription([

        Node(
            package='offline_replay',
            executable='camera_publisher',
            name='camera_publisher',

            parameters= [replay_config]
        )

    ])