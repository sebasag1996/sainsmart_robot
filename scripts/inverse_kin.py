#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Point
from std_msgs.msg import String
from std_msgs.msg import UInt16


L2 = 140		#Constant value for the first link of the robot
L3 = 152		#Constant value for the second link of the robot

global pointX
global pointY
global pointZ

def getPoint(cam_point):
	global pointX
	global pointY
	global pointZ
	pointX = cam_point.x
	pointY = cam_point.y
	pointZ = cam_point.z


def getTheta1(pointx,pointy):
	theta1 = math.atan2(pointy,pointx)
	theta1 = math.degrees(theta1)
	if (theta1 >=0) and (theta1 < 180):
		return theta1

def getTheta2(pointx,pointy,Pz):
	global L2
	global L3 
	D = math.sqrt(pointx*pointx + pointy*pointy + Pz*Pz)
	exp = ((D*D + L2*L2 - L3*L3)/(2*L2*D))

	d = math.sqrt(pointx*pointx + pointy*pointy)
	gamma = math.atan2(Pz,d)
	gamma = math.degrees(gamma)

	if (exp >= -1.0) and (exp <= 1.0):
		theta2 = math.acos(exp)
		theta2 = math.degrees(theta2) 
		theta2 = gamma + theta2
		return theta2
	else:
		return 0	#Error code for not reaching

def getTheta3(pointx,pointy,Pz):
	global L2
	global L3 
	D = math.sqrt(pointx*pointx + pointy*pointy + Pz*Pz)
	exp = ((L2*L2 + L3*L3 - D*D)/(2*L2*L3))

	if (exp >= -1.0) and (exp <= 1.0):
		theta3 = math.acos(exp)
		theta3 = math.degrees(theta3) 
		theta3 = math.fabs(theta3 - 180)
		return theta3
	else:
		return 0	#Error code for not reaching
	
		
	
def program():
	
	global pointX
	global pointY
	global pointZ
	pointZ = 1
	pointX = 1
	pointY = 1
	 

	rospy.init_node('inverse_kin', anonymous=True)
	rate = rospy.Rate(10)

	rospy.Subscriber("/effector_position", Point, getPoint)	#Check if the suscriber name is irrelevant and can be anyone


	pub_1 = rospy.Publisher('/servo1', UInt16, queue_size=10)	#Check the servo order 
	pub_2 = rospy.Publisher('/servo2', UInt16, queue_size=10)
	pub_3 = rospy.Publisher('/servo3', UInt16, queue_size=10)
	pub_4 = rospy.Publisher('/servo4', UInt16, queue_size=10)



	while not rospy.is_shutdown():
		if (pointX==0) or (pointZ==0):
			print "The points cannot be zero"
		else:
			theta1 = getTheta1(pointX,pointY)
			theta2 = getTheta2(pointX,pointY,pointZ)
			theta3 = getTheta3(pointX,pointY,pointZ)
			if (theta1 != -1):
				pub_1.publish(theta1)
			else:
				print "Object not rechable 	"#Publicate an error message 
			if (theta2 != 0):
				pub_2.publish(theta2)
			else:
				print "Object not reachable"	#Publicate an error message
	 
			if (theta3 != 0):
				pub_3.publish(theta3)
			else:
				print "Object not reachable"	#Publicate an error message 

		rate.sleep()

if __name__ == '__main__':
	program()
