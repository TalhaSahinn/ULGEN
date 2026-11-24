#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np



class Dron_tespit:
  def __init__(self):
    self.bridge=CvBridge()
    self.image_sub = rospy.Subscriber(
      "/robot/kamera/image_raw",
      Image,
      self.image_callback,
      queue_size = 1
    )


  def image_callback(self,msg):
    frame =self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")



    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    alt_kirmizi1 = np.array([0,120,70])
    ust_kirmizi1 = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, alt_kirmizi1,ust_kirmizi1)

    alt_kirmizi2 = np.array([170,120,70])
    ust_kirmizi2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, alt_kirmizi2, ust_kirmizi2)


    dron_mask = mask1 + mask2

    dron_mask = cv2.erode(dron_mask, None,  iterations = 2)
    dron_mask = cv2.dilate(dron_mask, None, iterations = 2)

    contours, _ = cv2.findContours(dron_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    durum_metni = "KIRMIZI GORUNMEDI"
    renk = (0,0,255)

    if contours:
      high_contour = max(contours, key=cv2.contourArea)
      if cv2.contourArea(high_contour) > 500:
        M = cv2.moments(high_contour)
        if M['m00'] != 0:
          center_x = int(M["m10"] / M["m00"])
          center_y = int(M["m01"] / M["m00"])
          durum_metni = f"KIRMIZI GORUNDU ({center_x} {center_y})"
          renk = (0,255,0)
          cv2.circle(frame ,(center_x, center_y) , 6 ,(255,0,0),-1)
          x,y,w,h = cv2.boundingRect(high_contour)
          cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)


    cv2.putText(
      frame,
      durum_metni,
      (15,35),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.8,
      renk,
      2,
    )


    cv2.imshow("kamera Akisi",frame)
    cv2.waitKey(1)







    cv2.imshow("kamera akisi", frame)
    cv2.waitKey(1)



if __name__ == '__main__':
  rospy.init_node("dron_tespit_node", anonymous = True)

  detector = Dron_tespit()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    cv2.destroyAllWindows()


