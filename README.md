# AlphaBot2-PiZero
## About
<img src="https://github.com/skyap/AlphaBot2-PiZero/blob/master/images/alphabot2-pizero-8.jpg" width="400"></br>
1. To create a easy to use API for students to interact with AlphaBot2-PiZero</br>
2. Students will be focus on the testing of algorithms on the robot instead of dealing with GPIO on Pi.</br>

official webpage:</br>
https://www.waveshare.com/wiki/AlphaBot2-PiZero</br>
## Overall project architecture 
<img src="https://github.com/skyap/AlphaBot2-PiZero/blob/master/images/flow.jpg" width="400"></br>
## **_WARNING!!_**
1. Do not run motors when power Pi Zero W from USB</br>
2. When weird behaviours occur, such as below, turn off power and charge your battery:</br>
	2.1. Servo work fine with your code but when you try it later with the same code it didn't work correctly.</br>
	2.2. Conectivity to Pi Zero W suddenly drop.</br>
3. AlpahBot2 have to be on the floor before you run any commands on motors.
4. Do not turn the servo with hand, before and after start main.py. It will break the servo. Refer to <a href="https://arduino.stackexchange.com/questions/4076/what-is-commonly-done-to-stop-a-servo-after-reaching-desired-position">what is commonly done to stop a servo after reaching desired position</a></br></br>
"**_A servo is always running. In a general sense, the servo is a control loop that takes as input a position target and applies force to hold at the requested target._**"


## Softwares and libries required on PC/ Laptop
1. python3+ 
2. numpy (not required for the moment)
3. opencv (not required for the moment)
4. IDE (PyCharm, IDLE, Stani's Python Editor, Spyder, Jupyter Notebook, Notepad, Notepad++, etc.)
## Library required on PiZero W 
```
$ pip3 install psutil
$ sudo apt install lsof
```
## Python learning resources
if you are new to python, below is the best beginner course for you:</br>
https://www.coursera.org/learn/python

## Program required on PC/ Laptop
1. VNC Viewer(if the Pi running GUI)</br>
2. PuTTY(for window user)/ SSH (for linux user)</br>



## Router settings for PiZero W
1. Use WPA or WPA2 only
2. Ensure it is 2.4GHz

## Step for connect to another WIFI
```
$ cd /etc/wpa_supplicant
$ sudo nano wpa_supplicant.conf
```
put below in the the file:</br>
```
network={
	ssid="Robot"
	psk="1234567890"
	priority=1
	scan_ssid=1
}
```

change the **_ssid_** and **_psk_** to your router id and password</br>
after finish press **CTRL+x**, **y**, **ENTER**
## Before start
1. Download latest repository from https://github.com/skyap/AlphaBot2-PiZero
2. On AlphaBot2-PiZero or laptop, open terminal and type:</br>
```
$ git clone https://github.com/skyap/AlphaBot2-PiZero
```
3. Alternatively , downlaod and unzip the folder

## Step for connect to AlphaBot2-PiZero
1. Power up AlphaBot2-PiZero (USB or batteries)
2. Connect to router "Robot", password: 1234567890
3. Look for IP of your robot's name in the _DHCP Client Table_, for example: 192.168.1.101
4. Open VNC Viewer
5. Navigate to File > New Connections, type the IP in VNC Server, press OK, double click on the new icon</br></br>
6. <img src="https://github.com/skyap/AlphaBot2-PiZero/blob/master/images/vnc1.JPG" width="400"></br>
7. User Name: pi</br>
8. Password: raspberry</br>

## Step for start up socket server
1. From Destop, navigate to Documents > Servers</br> 
2. Tools > Open Current Folder in Terminal</br>
<img src="https://github.com/skyap/AlphaBot2-PiZero/blob/master/images/vnc2.JPG" width="400"></br>
3. Modify main.py if you are not going to run all the socket servers
4. Type below in the terminal</br>
```
$ python3 main.py
```
## Step to shutdown socket server
**_CTRL+c_** or **_CTRL+z_**
## Step to shutdown AlphaBot2-PiZero
1. Similiar to how you shutdown Windows

## Issues
1. In ad-hoc mode, some time connection establish is not good. If you can't VNC, PuTTY/SSH or FileZilla into Pi after ad-hoc connection, try to disconnect and reconnect again.</br></br>
2. OSError: [Errno 98] Address already in use 
``` 
$ sudo netstat -nlp | grep 8000
$ sudo kill -9 123
```

## Functions
### <u>line tracker</u>
```python
from line_tracker import line_tracker</br>
import time</br>
# IP adddress of your robot
address  = "192.168.1.100"
# create line tracker object
lt = line_tracker(address)
# start reading data from server
lt.start()</br>
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
### <u>motor</u>
```python
from motor import motor
import time
address = "192.168.1.100"
mot = motor(address)

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

## Robot basic
1. Type of turning</br>
<img src="https://github.com/skyap/AlphaBot2-PiZero/blob/master/images/robot_turn.jpg" width="400">

## Assignments:
1. Straight line 
2. Straight line to and fro
3. T - junctions to and fro
4. ???
5. ???


	
	