from camera_server import camera
from ultrasonic_server import ultrasonic
from infrared_server import infrared
from servo_server import servo
from motor_server import motor
from line_tracker_server import line_tracker

import psutil
from psutil import process_iter
import subprocess
import time


#all_server = [camera,ultrasonic,infrared,servo,motor,line_tracker]
all_server = [ultrasonic,infrared,motor,line_tracker]

# release port before start if it in use
def release_ports(ports):
	for proc in process_iter():
		try:
			for conns in proc.connections(kind='inet'):
				if conns.laddr.port in ports:
					print("kill process at port: ",conns.laddr.port)
					subprocess.call(['./release_port.sh',str(conns.laddr.port)])
		except psutil.AccessDenied:
			continue
subprocess.check_call(['chmod','+x','release_port.sh'])
all_port = ['8000','8001','8002','8003','8004','8006'] 
release_ports(all_port)



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


