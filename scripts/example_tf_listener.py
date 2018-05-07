#!/usr/bin/env python  
import rospy
import numpy
import tf
from tf.transformations import * #Import function to transform quat to angles
import geometry_msgs.msg

"""This is an example of how to implement a tf listener
   
   This listener hears the transformation from /world frame to /marker frame and prints the results.
   If the frames does not exist it will publish a warning. 
"""
if __name__ == '__main__':
    rospy.init_node('example_tf_listener')
    listener = tf.TransformListener() #Creates the tf listener
    rate = rospy.Rate(10.0) #10Hz rate
    while not rospy.is_shutdown():
        try:
        #!-- 'marker', 'map'
            (trans,quat) = listener.lookupTransform('/world', '/marker', rospy.Time(0)) 
            #use the listener to 'hear' the transformation from world to marker
            #trans ->position x,y,z
            #rot -> quaternion qx, qy, qz, qw
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print "Some tf exception happened, it is possible that the frames are not beeing published"
            rate.sleep()
            continue
            
        x = trans[0]
        y = trans[1]
        z = trans[2]
        rot=euler_from_quaternion(quat)
        rotx = rot[0]
        roty= rot[1]
        rotz= rot[2]
        
        print "x:", x, " y:", y, " z:", z,
        print "rotations x,y,z", rot
       
        
        rate.sleep()
