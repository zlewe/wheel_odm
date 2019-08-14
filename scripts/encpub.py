#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import Int16
import re

COM_PORT = '/dev/ttyUSB0'
BAUD_RATES = 57600
ser = serial.Serial(COM_PORT, BAUD_RATES)
for i in range(5):
        garbage=ser.readline()

def encoder():
	pub_l = rospy.Publisher('lwheel', Int16, queue_size=10)
	pub_r = rospy.Publisher('rwheel', Int16, queue_size=10)
        rospy.init_node('encpub_py')
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
                while ser.in_waiting:
                        data = ser.readline()
                        if(data[0]!='t'):
                                result = re.sub("[^0-9-,]","",data)
                                enc=re.split('[,]',result)

                                l=int(enc[0])
                                r=int(enc[1])
                                pub_l.publish(l)
				pub_r.publish(r)
			
if __name__ == '__main__':
	try:
		encoder()
	except rospy.ROSInterruptException:
		ser.close()
		pass
