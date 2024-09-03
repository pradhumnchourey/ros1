#! /usr/bin/env python3
import rospy
import geometry_msgs
import tf2_ros
import math

def broadcast_dynamic_transform():
    rospy.init_node("dynamic_transform_broadcaster")
    broadcaster = tf2_ros.TransformBroadcaster()

    transform = geometry_msgs.msg.TransformStamped()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        transform.header.stamp = rospy.Time.now()
        transform.header.frame_id = "base_link"
        transform.child_frame_id = "gripper_link"

        transform.transform.translation.x = 0.2*math.sin(rospy.Time.now().to_sec())
        transform.transform.translation.y = 0.0
        transform.transform.translation.z = 0.5

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = 0.0
        transform.transform.rotation.w = 1.0

        broadcaster.sendTransform(transform)

        rate.sleep()

if __name__ == '__main__':
    try:
        broadcast_dynamic_transform()
    except rospy.ROSInterruptException as e:
        rospy.logwarn(e)