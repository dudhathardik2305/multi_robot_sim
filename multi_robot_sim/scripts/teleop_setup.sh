
#!/bin/bash
echo "Use arrow keys to control robots. Open new terminals for each robot."
gnome-terminal -- bash -c "ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/robot1; exec bash"
gnome-terminal -- bash -c "ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/robot2; exec bash"
gnome-terminal -- bash -c "ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/robot3; exec bash"
