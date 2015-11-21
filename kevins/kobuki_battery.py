#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

# Monitor the kobuki's battery level

import roslib
import rospy
from go_to_specific_point_on_map import GoToPose #for specific locations
from kobuki_msgs.msg import SensorState

class kobuki_battery():

	kobuki_base_max_charge = 160

	def __init__(self):
		rospy.init_node("kobuki_battery")		

		#monitor Kobuki's power and charging status.  If an event occurs (low battery, charging, not charging etc) call function SensorPowerEventCallback
	        rospy.Subscriber("/mobile_base/sensors/core",SensorState,self.SensorPowerEventCallback)

		#rospy.spin() tells the program to not exit until you press ctrl + c.  If this wasn't there... it'd subscribe and then immediatly exit (therefore stop "listening" to the thread).
		rospy.spin();


	def SensorPowerEventCallback(self,data):
		rospy.loginfo("Kobuki's battery is now: " + str(round(float(data.battery) / float(self.kobuki_base_max_charge) * 100)) + "%")
		if(int(data.charger) == 0) :
			rospy.loginfo("Not charging at docking station")
			if(data.battery<20): #go to the charging dock if battery value is less than 20
				GoToPose(x1,y1)
				print "lunchbot is now going home"
		else:
			rospy.loginfo("Charging at docking station")
	

if __name__ == '__main__':
	try:
		kobuki_battery()
	except rospy.ROSInterruptException:
		rospy.loginfo("exception")
