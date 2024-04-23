import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class KochSnowflakeBot(Node):
    def __init__(self):
        super().__init__('koch_snowflake_bot')
        self.twist_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        self.pose = None
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.cb_pose,
            10)

        self.declare_parameter('speed', 1.0)
        self.declare_parameter('omega', 20.0)

    def cb_pose(self, msg):
        self.pose = msg



    def go_straight(self, distance):
        speed = self.get_parameter('speed').get_parameter_value().double_value
        vel_msg = Twist()
        if distance > 0:
            vel_msg.linear.x = speed
        else:
            vel_msg.linear.x = -speed
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0

        # Set loop rate
        loop_rate = self.create_rate(100, self.get_clock()) # Hz

        # Calculate time
        T = abs(distance/speed)     # s

       # Publish first msg and note time
        #self.get_logger().info('Turtle started.')
        self.twist_pub.publish(vel_msg)
        when = self.get_clock().now() + rclpy.time.Duration(seconds=T)

       # Publish msg while the calculated time is up
        while (self.get_clock().now() < when) and rclpy.ok():
            self.twist_pub.publish(vel_msg)
           #self.get_logger().info('On its way...')
            rclpy.spin_once(self)   # loop rate

       # Set velocity to 0
        vel_msg.linear.x = 0.0
        self.twist_pub.publish(vel_msg)
       #self.get_logger().info('Arrived to destination.')

    def turn(self, angle):
        omega = self.get_parameter('omega').get_parameter_value().double_value
        vel_msg = Twist()

        vel_msg.linear.x = 0.0
        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        if angle > 0:
            vel_msg.angular.z = math.radians(omega)
        else:
            vel_msg.angular.z = math.radians(-omega)

       # Set loop rate
        loop_rate = self.create_rate(100, self.get_clock()) # Hz

       # Calculate time
        T = abs(angle/omega)     # s

       # Publish first msg and note time
       #self.get_logger().info('Turtle started.')
        self.twist_pub.publish(vel_msg)
        when = self.get_clock().now() + rclpy.time.Duration(seconds=T)

       # Publish msg while the calculated time is up
        while (self.get_clock().now() < when) and rclpy.ok():
            self.twist_pub.publish(vel_msg)
           #self.get_logger().info('On its way...')
            rclpy.spin_once(self)   # loop rate

       # Set velocity to 0
        vel_msg.angular.z = 0.0
        self.twist_pub.publish(vel_msg)
       #self.get_logger().info('Arrived to destination.')

    #def draw_koch_snowflake(self, order, length):
     #      for _ in range(3):
      #         self.draw_koch_curve(order, length)
       #        self.turn(-120)

    def draw_koch_curve(self, order, length):
        if order == 0:
            self.go_straight(length)
        else:
            self.draw_koch_curve(order - 1, length / 3)
            self.turn(60)
            self.draw_koch_curve(order - 1, length / 3)
            self.turn(-120)
            self.draw_koch_curve(order - 1, length / 3)
            self.turn(60)
            self.draw_koch_curve(order - 1, length / 3)

    def sierpinski(self, order, length):
        if order == 0:
            return
        else:
            for i in range(0,3):
                self.go_straight(length)
                self.sierpinski(order-1,length/2)
                self.go_straight(-length)
                self.turn(120)

def main(args=None):
    rclpy.init(args=args)

    koch_bot = KochSnowflakeBot()

    # Draw a Koch snowflake with order 3 and size 5
    koch_bot.sierpinski(4, 2.0)

    rclpy.spin(koch_bot)

    koch_bot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
