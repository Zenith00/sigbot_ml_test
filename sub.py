

import rospy
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import cv2
from sensor_msgs.msg import Image

bridge = CvBridge()

def callback(data):
    print("Asdf")
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')

    cv2.imshow('display', cv_image)
    cv2.waitKey(30)

def listener():


    rospy.init_node('video_listen')


    rospy.Subscriber('/video', Image, callback)

    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()
