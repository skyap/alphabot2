#from camera import camera
from ultrasonic import ultrasonic
from infrared import infrared
from line_tracker import line_tracker
#import cv2
import time
address='192.168.1.1'
#cam = camera(address)
#cam.start()
inf = infrared(address)
inf.start()
ult = ultrasonic(address)
ult.start()
lt = line_tracker(address)
lt.start()
inf_t = time.time()




while True:
	try:
		t = time.time()
		# if cam.image!=[]:
		# 	cv2.imshow("image",cam.image)
		# 	cv2.waitKey(1)
		if t-inf_t>1:
			print("infrared left,right: ",inf.left,inf.right)
			print("ultrasonic: ",ult.measurement)
			print("line_tracker: ",lt.data)
			inf_t = t
			
	except KeyboardInterrupt:
		#cam.stop()
		inf.stop()
		ult.stop()
		lt.stop()
		# cv2.destroyAllWindows()
		break




