#! /usr/bin/env python3

import rospy
import geometry_msgs.msg
import tf2_geometry_msgs
import tf2_ros

rospy.init_node("tf2_listner")

tf_buffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tf_buffer)

rate = rospy.Rate(10.0)

while not rospy.is_shutdown():
    try:
        # Query the transformation from gripper_link to base_link
        transform = tf_buffer.lookup_transform("base_link", "gripper_link", rospy.Time(0))

        point_in_gripper_frame = geometry_msgs.msg.PointStamped()
        point_in_gripper_frame.header.frame_id = "gripper_link"
        point_in_gripper_frame.point.x = 1.0
        point_in_gripper_frame.point.y = 0.0
        point_in_gripper_frame.point.z = 0.0

        point_in_base_form = tf_buffer.transform(point_in_gripper_frame, "base_link")
        rospy.loginfo(point_in_base_form)

    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        continue

    rate.sleep()