#! /usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')

    rospy.loginfo("Hello from test_node")
    # rospy.logwarn("This is a warning")
    # rospy.logerr("This is an error")
    # rospy.sleep(3.0)
    # rospy.loginfo("End of program")

    rate=rospy.Rate(1)     # 1Hz, i.e. it will print Hello once every second

    while not rospy.is_shutdown():      #until the node is alive, i.e. until we don't kill it 
        rospy.loginfo("Hello")
        rate.sleep()
