#! /usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo(msg)

if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    #Subscriber is going to listen to a topic and when we receive a message from the topic,
    # a callback function will be called to process the message

    rospy.loginfo("Node has started")
    rospy.spin()