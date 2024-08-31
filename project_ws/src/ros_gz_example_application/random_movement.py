#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class RandomMovement(Node):
    def __init__(self):
        super().__init__('randommovement')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_randomly)

    def move_randomly(self):
        msg = Twist()
        # Set random forward speed between 0 and 0.5 m/s (no backward movement)
        msg.linear.x = random.uniform(0, 0.5)  # Random forward speed only
        msg.angular.z = random.uniform(-1.0, 1.0)  # Allow random rotation
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    random_movement = RandomMovement()
    rclpy.spin(random_movement)
    random_movement.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
