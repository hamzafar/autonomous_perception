#!/bin/bash

echo "Activating CARLA environment..."
source ~/autonomous_vision/carla_env/bin/activate

echo "Sourcing ROS2..."
source /opt/ros/humble/setup.bash
source ~/ros-bridge/install/setup.bash

echo "Setting DDS environment..."
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export ROS_DOMAIN_ID=0
export ROS_LOCALHOST_ONLY=1
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST

echo "Setting CARLA Python path..."
export PYTHONPATH=$PYTHONPATH:/home/hamza/autonomous_vision/carla_env/lib/python3.10/site-packages

echo "Launching CARLA ROS Bridge..."
ros2 launch carla_ros_bridge carla_ros_bridge.launch.py \
host:=localhost \
timeout:=30 \
passive:=True \
synchronous_mode:=False
