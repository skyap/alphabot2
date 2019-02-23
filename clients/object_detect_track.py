#https://www.hackster.io/mjrobot/automatic-vision-object-tracking-5575c4

import time
from servo import servo
from camera import camera
import cv2
import math



ser=servo()
cam=camera()
cam.start()
hangle=90
vangle=90
ser.horizontal(hangle)
ser.vertical(vangle)

readings_x = []
readings_y = []
def sma(x,y):
	global readings_x
	global readings_y
	readings_x.append(x)
	readings_y.append(y)
	x = sum(readings_x)/max(len(readings_x),1)
	y = sum(readings_y)/max(len(readings_y),1)
	if len(readings_x) == 10:
		readings_x.pop(0)
		readings_y.pop(0)
		
	return x,y
		
	

def map_servo_position(x,y):
	global hangle
	global vangle
	if x<200:
		hangle+=2
		if hangle>170:
			hangle=170
		ser.horizontal(hangle)
	if x>280:
		hangle-=2
		if hangle<10:
			hangle = 10
		ser.horizontal(hangle)
	if y>360:
		vangle+=2
		if vangle>110:
			vangle = 110
		ser.vertical(vangle)
	if y<280:
		vangle-=2
		if vangle<10:
			vangle=10
		ser.vertical(vangle)
	time.sleep(0.1)
	
# to be determine using interactive_color_segment.py
while cam.image==[]:
	pass
width,height,_ = cam.image.shape
print(width,height)
color_lower = (23,70,106)
color_upper = (43,255,187)

try:	
	while True:

		image = cam.image
		hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		
		mask = cv2.inRange(hsv,color_lower,color_upper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[1]
		center = None
		
		if len(cnts)>0:
			c = max(cnts,key=cv2.contourArea)
			((x,y),radius) = cv2.minEnclosingCircle(c)
			x=int(x)
			y=int(y)
			radius=int(radius)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			if radius >30:					
				cv2.circle(image,(x,y),radius,(0,255,255),2)
				cv2.circle(image,center,5,(0,255,255),-1)
				cv2.putText(image,str(x)+","+str(y)+",R"+str(radius),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
				map_servo_position(x,y)
		cv2.imshow("image",image)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
finally:
	cv2.destroyAllWindows()
	cam.stop()
		
		
		
		
		
		
		
		
	
