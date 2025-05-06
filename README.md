# -multi_robot_sim
📦 multi_robot_sim, ROS 2 Humble + Gazebo Fortress


bash

unzip multi_robot_sim.zip
cd multi_robot_sim

Make teleop script executable:

bash
chmod +x scripts/teleop_setup.sh

Build the package:

bash
colcon build --packages-select multi_robot_sim
source install/setup.bash

Launch Gazebo and spawn robots:

bash
ros2 launch multi_robot_sim spawn_robots.launch.py

Start manual control (in separate terminal):

bash
./scripts/teleop_setup.sh