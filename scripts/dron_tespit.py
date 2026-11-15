import cv2
import numpy as np

def hedef_dron(frame):
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


	if contours:
		high_contour = max(contours, key=cv2.contourArea)
		


		if cv2.contourArea(high_contour) > 500:
			M = cv2.moments(high_contour)

			if M['m00'] != 0:
				center_x = int(M["m10"] / M["m00"])
				center_y = int(M["m01"] / M["m00"])
				return center_x , center_y


	return None ,None



if __name__ == '__main__':
	resim = cv2.imread("test2.png")


	if resim is not None:
		x, y = hedef_dron(resim)
		

		if x is not None and y is not None:
			print (f"Basarali Hedefin merkez koordinatlari X={x} Y={y}")
			cv2.circle(resim, (x,y),5,(0,255,0),-1)
		else:
			print("ekranda yeterli buyuklukte kirmizi hedef bulunamadi")

		cv2.imshow("Test Ekrani", resim)
		cv2.waitkey(0)
		cv2.destroyAllWindows()
	else:
		print("hata resim bulunamadi")









