#!/usr/bin/env python

import rospy
import actionlib
from counting_example.msg import CountAction, CountGoal, CountResult, CountFeedback

def feedback_cb(feedback):
    rospy.loginfo("Feedback: %s" % feedback.feedback)

def done_cb(state, result):
    rospy.loginfo("Result: %s" % result.result)
    rospy.signal_shutdown("Action complete")

def main():
    rospy.init_node('count_action_client')

    # Create an action client
    client = actionlib.SimpleActionClient('count_action', CountAction)

    # Wait for the server to start
    rospy.loginfo("Waiting for action server to start.")
    client.wait_for_server()

    # Create a goal to send to the action server
    goal = CountGoal(order=5)
    rospy.loginfo("Sending goal.")
    client.send_goal(goal, feedback_cb=feedback_cb, done_cb=done_cb)

    # Wait for the result
    rospy.spin()

if __name__ == '__main__':
    main()