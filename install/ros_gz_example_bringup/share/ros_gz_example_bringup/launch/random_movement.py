#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random
import time

class RandomMovement(Node):
    def __init__(self):
        super().__init__('random_movement')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_randomly)  # Change frequency as needed

    def move_randomly(self):
        msg = Twist()

        # Generate random linear and angular velocities
        msg.linear.x = random.uniform(-0.5, 0.5)
        msg.angular.z = random.uniform(-1.0, 1.0)

        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: Linear X: {msg.linear.x}, Angular Z: {msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)
    random_movement = RandomMovement()
    rclpy.spin(random_movement)
    random_movement.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()