#!/usr/bin/env python
import roslib
# roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cv_bridge = CvBridge()


def main():
    cap = cv2.VideoCapture("/home/austin/Downloads/underwatertest.mp4")

    image_pub = rospy.Publisher("video", Image, queue_size=10)
    rospy.init_node("video_pub")

    frame_counter = 0
    rate = rospy.Rate(5)
    while True:
        ret,frame = cap.read()
        cv2.imshow('displayin', frame)
        cv2.waitKey(30)

        frame_counter += 1
        # If the last frame is reached, reset the capture and the frame_counter
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            frame_counter = 0  # Or whatever as long as it is the same as next line
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if ret:
            image_pub.publish(cv_bridge.cv2_to_imgmsg(frame, 'bgr8'))
            print(frame_counter)
        else:
            print("Fail")
        rate.sleep()
    # rospy.spin()


main()
