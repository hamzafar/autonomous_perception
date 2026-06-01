#!/bin/bash

source /opt/ros/humble/setup.bash
source ~/ros-bridge/install/setup.bash

export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST

echo "ROS2 environment sourced successfully."
