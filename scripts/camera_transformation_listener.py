#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg



if __name__ == '__main__':

    cam_point = geometry_msgs.msg.Point()
    rospy.init_node('camera_tf_listener')

    listener = tf.TransformListener()
    
    effector_position_publisher = rospy.Publisher('effector_position', geometry_msgs.msg.Point,queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/marker', '/map', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
            
        cam_point.x = trans[0]
        cam_point.y = trans[1]
        cam_point.z = trans[2]
        
        effector_position_publisher.publish(cam_point)

        rate.sleep()
