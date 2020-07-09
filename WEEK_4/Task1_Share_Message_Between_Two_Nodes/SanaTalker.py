#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def SanaTalker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('SanaTalker', anonymous=False)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		Sana_Hello = "hello Robot, How are you?"
		rospy.loginfo(Sana_Hello)
		pub.publish(Sana_Hello)
		rate.sleep()

if __name__ == '__main__':
	try:
		SanaTalker()
	except rospy.ROSInterruptException:
		pass
