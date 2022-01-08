#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

f = 0

def cb(message):
    global f
    f = message.data*100
    
if __name__ == '__main__':
    rospy.init_node('100times')
    sub = rospy.Subscriber('count_up', Int32, cb) 
    pub = rospy.Publisher('100times', Int32, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(f)
        rate.sleep()
