#!/usr/bin/env python2

moves =    [[0,  90],
            [20,  0],
            [0,  -90],
            [20, 0],
            [0,  90],
            [100,0],
            [0,  90],
            [20, 0],
            [0,  -90],
            [20, 0],
            [0,  -90],
            [50, 0],
            [0,  -45],
            [70, 0],
            [0,  90],
            [70, 0],
            [0,  -45],
            [50, 0],
            [0,  -90],
            [20,  0],
            [0,  -90],
            [20, 0],
            [0,  90],
            [100,0],
            [0,  90],
            [20, 0],
            [0,  -90],
            [20, 0],
            [0,  -90],
            [60, 0],
            [0,  -90],
            [20, 0],
            [0,  -90],
            [20, 0],
            [0,  90],
            [100, 0],
            [0,  135],
            [85, 0],
            [0,  -90],
            [85, 0],
            [0,  135],
            [100, 0],
            [0,  90],
            [20, 0],
            [0,  -90],
            [20, 0],
            [0,  -90],
            [60, 0]
         ]

import rospy
from geometry_msg.Twist import Twist

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    vel = Twist()
    i = 0
    while not rospy.is_shutdown() and i < len(moves):
        pub = rospy.Publisher('/turtle1/cmd_vel',
                          Twist, queue_size=10)
        vel.linear.x = moves[i][0]
        vel.linear.y = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = moves[i][1]
        rospy.loginfo("Move #%f", i)
        i += 1
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass