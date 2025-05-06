
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    ld = LaunchDescription()
    for i in range(3):  # Change to 4 if needed
        robot_name = f'robot{i+1}'
        robot_ns = f'/{robot_name}'
        ld.add_action(Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name=f'spawn_{robot_name}',
            arguments=['-entity', robot_name, '-file', os.path.join(
                os.getenv('HOME'), 'multi_robot_sim/models/simple_bot/model.sdf'),
                '-x', str(i * 2), '-y', '0', '-z', '0'],
            output='screen',
            namespace=robot_ns
        ))
    return ld
