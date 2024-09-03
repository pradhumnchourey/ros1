#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen

#define a global variable
previous_x=0

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose):
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x=1.0
        cmd.angular.z=1.4
    else:
        cmd.linear.x=5.0
        cmd.angular.z=0.0
    pub.publish(cmd)

    global previous_x
    if pose.x>=5.5 and previous_x<5.5:
        rospy.loginfo("Set color to red!")
        call_set_pen_service(255, 0, 0, 3, 0)
    elif pose.x<5.5 and previous_x>5.5:
        rospy.loginfo("Set color to green!")
        call_set_pen_service(0, 255, 0, 3, 0)
    previous_x=pose.x
    #if we don't use previous_x, set_pen_service will be called everytime the value of pose.x cahnges 
    # and even for minor changes of 0.1 it will call the service, which will be heavy on the program,
    # so we define a variable previous_x, and we'll only call the service when the value of pervious_x changes
    # topics can be called at a higher frequency but not services. 

if __name__=='__main__':
    rospy.init_node("turtle_controller")
    # wait for the service set_pen to start
    rospy.wait_for_service("/turtle1/set_pen")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.loginfo("Turtle Controller started")
    rospy.spin()