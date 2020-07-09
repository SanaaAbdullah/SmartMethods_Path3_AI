#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data + " Hi, I am fine thanks! ")
	   
def RobotListener():
	rospy.init_node('RobotListener', anonymous=False)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

if __name__ == '__main__':
	RobotListener()
