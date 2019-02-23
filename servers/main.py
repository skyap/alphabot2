from camera_server import camera
from ultrasonic_server import ultrasonic
from infrared_server import infrared
from servo_server import servo
from motor_server import motor
from line_tracker_server import line_tracker
import time

all_server = [camera,ultrasonic,infrared,servo,motor,line_tracker]

threads=[]
for i in all_server:
	thread = i()
	thread.daemon = True
	thread.start()
	threads.append(thread)
print("All Servers Running")

while True:
	try:
		time.sleep(100)
	except:
		break
for i in threads:
	#i.stop()
	i.kill=True


print("All Servers Killed")	


