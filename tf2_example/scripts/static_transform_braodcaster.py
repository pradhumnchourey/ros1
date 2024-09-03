#! /usr/bin/env python3

import rospy
import tf2_ros
import geometry_msgs

def broadcast_static_transform():
    rospy.init_node("static_transform_broadcaster")
    broadcaster = tf2_ros.StaticTransformBroadcaster()

    static_transform = geometry_msgs.msg.TransformStamped()

    static_transform.header.stamp = rospy.Time.now()
    static_transform.header.frame_id = "base_link" 
    static_transform.child_frame_id = "camera_link"

    static_transform.transform.translation.x = 0.5
    static_transform.transform.translation.y = 0.5
    static_transform.transform.translation.z = 0.0

    static_transform.transform.rotation.x = 0.0
    static_transform.transform.rotation.y = 0.0
    static_transform.transform.rotation.z = 0.0
    static_transform.transform.rotation.w = 1.0

    broadcaster.sendTransform(static_transform)

    rospy.loginfo("Static transform from base_link to camera_link broadcasted")
    rospy.spin()

if __name__ == '__main__':
    try:
        broadcast_static_transform()
    except rospy.ROSInterruptException as e:
        rospy.logwarn(e)
