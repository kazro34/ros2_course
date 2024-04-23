from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle2',
            output='screen',
        ),
        Node(
            package='ros2_course',
            executable='turtlesim_controller1',
            name='turtlesim_controller1',
            output='screen',
        ),

    ])


