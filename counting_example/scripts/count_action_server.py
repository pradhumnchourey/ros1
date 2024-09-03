#!/usr/bin/env python

import rospy
import actionlib
from counting_example.msg import CountAction, CountResult, CountFeedback

class CountActionServer(object):
    _feedback = CountFeedback()
    _result = CountResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer("count_action", CountAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

    def execute_cb(self, goal):
        r = rospy.Rate(1)
        success = True

        for i in range(goal.order):
            if self._as.is_preempt_requested():
                rospy.loginfo("Preempted")
                self._as.set_preempted()
                success = False
                break

            self._feedback.current_count = i
            self._as.publish_feedback(self._feedback)
            r.sleep()

        if success:
            self._result.final_count = goal.max_count
            rospy.loginfo("Succeeded")
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('count_action_server')
    server = CountActionServer()
    rospy.spin()
