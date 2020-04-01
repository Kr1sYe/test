#!/usr/bin/env python
# coding=utf-8

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('joint_msgs', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    
    while not rospy.is_shutdown():
        
        hello_str = "movej(180.123, 180.456, 0.789, 180.123, 0.456, 60.012)(0.123, 0.123, 0.123, 0.0, 5.0, 1.0)"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
