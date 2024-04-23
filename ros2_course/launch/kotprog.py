import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_launch = IncludeLaunchDescription(
       PythonLaunchDescriptionSource(
           os.path.join(get_package_share_directory('ros2_course'),
                        'turtlesim_world_1.py'))
    )

    turtlesim_launch = IncludeLaunchDescription(
       PythonLaunchDescriptionSource(
           os.path.join(get_package_share_directory('ros2_course'),
                        'turtlesim_launch.py')
        )
    )

    ld.add_action(turtlesim_world_1)
    ld.add_action(turtlesim_launch)
    return ld
