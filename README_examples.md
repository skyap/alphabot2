# Codes Examples
## <u>line tracker</u>
```python
from alphabot2 import motor,line_tracker
import time
# IP adddress of your robot
address  = "192.168.0.100"
# create line tracker object
lt = line_tracker.line_tracker(address)
# start reading data from server
lt.start()
for i in range(100):
	# stop for one second
	time.sleep(1)
	if lt.data==0:
		continue
	# lt.data is an array with 5 elements
	print(lt.data)
# remember to stop the socket connection
lt.stop()
```
## <u>motor</u>
```python
from alphabot2 import motor,line_tracker
import time
address = "192.168.0.100"
mot = motor.motor(address)

# below is the general function's parameters and range
# mot.command(direction,speed,duration)
# parameters:
# direction: "forward","backward","left","right","set_left_speed","set_right_speed","stop"
# speed: 0-100
# duration: second

# run forward at 20 speed for 5 seconds
mot.command("forward",20,5)

# set speed of left and right and ask robot to move forward
mot.command("set_left_speed",10)
mot.command("set_right_speed",10)
mot.command("forward")
time.sleep(5)
# stop moving , speed set to zero
mot.command("stop")
time.sleep(1)

# set speed of left and right and ask robot to move backward
mot.command("set_left_speed",10)
mot.command("set_right_speed",10)
mot.command("backward")
time.sleep(5)
mot.command("stop")
time.sleep(1)

# spin turn  
mot.command("set_left_speed",10)
mot.command("set_right_speed",10)
mot.command("left")
time.sleep(5)
mot.command("stop")
time.sleep(1)

# spin turn 
mot.command("set_left_speed",10)
mot.command("set_right_speed",10)
mot.command("right")
time.sleep(5)
mot.command("stop")

# remember to stop the socket connection
mot.stop()
```
