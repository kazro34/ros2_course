from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from turtle import Screen, Turtle
import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TurtleGoToGoal(Node):
    def __init__(self):
        super().__init__('turtle_go_to_goal')

        self.cmdvel_pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)

        self.pose_subs = self.create_subscription(Pose,'/turtle1/pose',self.cb_pose,10)

        timer_period = 0.5

        self.timer = self.create_timer(timer_period,self.move2goal)

        self.pose=Pose()
        self.flag=False


    def cb_pose(self, data):
            self.pose.x = data.x
            self.pose.y = data.y
            self.pose.theta = data.theta
            msg='X: {:.3f},Y: {:.3f},Theta: {:.3f}'.format(data.x,data.y,data.theta)
            self.get_logger().info(msg)

    def euclidien_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x),2) + pow((goal_pose.y - self.pose.y),2))

    def liner_vel(self, goal_pose, constant=2):
        return constant*self.euclidien_distance(goal_pose)

    def steering_angle(self.goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=2):
        return constant*(self.steering_angle(goal_pose)-self.pose.theta)

    def move2goal(self, x, y):

        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y

        distance_tolerance = 0.1


        vel_msg=Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = self.angular_vel(goal_pose)

            self.cmdvel_pub.publish(vel_msg)

if __name__ == '__main__':
    main()
