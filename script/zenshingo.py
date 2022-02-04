#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios


def zenshin():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('zenshin_node')
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.1
        #rospy.loginfo(hello_str)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        zenshin()
    except rospy.ROSInterruptException:
        pass