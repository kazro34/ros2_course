# TurtleSim fractal drawer
Semester assignment in ros2

## About
These packages can draw 2 different fractals, the Koch snowflake, and an another snawflake desing. There is also an implementation of propotional controller in python.

### Usage

To Build this packages use the following commands:

    cd ~/ros2_ws
    colcon build --symlink-install

To run the packages you need to be in the correct folder

    cd ~/ros2_ws

And then you can run both of the launch files:

    ros2 launch ros2_course turtlesim_world_1.py
    ros2 launch ros2_course turtlesim_launch.py

