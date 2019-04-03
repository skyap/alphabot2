# alphabot2
https://github.com/skyap/alphabot2/README_python_installation.md
## About
<img src="https://github.com/skyap/alphabot2/blob/master/images/alphabot2-pizero-8.jpg" width="400"></br>
1. To create a easy to use API for students to interact with alphabot2</br>
2. Students will be focus on the testing of algorithms on the robot instead of dealing with GPIO on Pi.</br>

official webpage:</br>
https://www.waveshare.com/wiki/alphabot2</br>
## Install, Upgrade and Uninstall
1. install the libaries
```
pip install git+https://github.com/skyap/alphabot2.git
```
2. if you have install previously and wish to upgrade
```
pip install upgrade git+https://github.com/skyap/alphabot2.git
```
3. to uninstall it
```
pip uninstall alphabot2
```
4. to test your installation, open terminal or cmd
```
$ python
>>> import alphabot2
```
if it import sucessfully, that mean you install correctly
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

## Python learning resources
if you are new to python, below is the best beginner course for you:</br>
https://www.coursera.org/learn/python

## Program required on PC/ Laptop
1. PuTTY(for window user)/ SSH (for linux user)</br>

## Step for connect to AlphaBot2-PiZero
1. Power up alphabot2 (USB or batteries)
2. After you hear a beep, the robot is ready to go

## Functions
### <u>line tracker</u>
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
### <u>motor</u>
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

## Robot basic
1. Type of turning</br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/robot_turn.jpg" width="400"></br>
2. Spin turn by setting both wheel speed similiar(plus and minus based on your experience) and send left or right command
3. Pivot turn by setting one wheel speed and send left or right command

## Background of line following robot:
1. Below are some of the earliest maze solver robots.</br>
http://cyberneticzoo.com/tag/amazing-micromouse-maze-contest/</br>
http://cyberneticzoo.com/wp-content/uploads/2011/08/Emily-Popular-Electronics-Mar-1962.pdf
2. Maze solver is actually SLAM(simultaneous localization and mapping). However we are not going to do mapping in the assignment(encoder is required). We will only solve localized shortest path.

## Assignments:
1. Straight line 
2. Straight line to and fro</br>
[![Watch the video](https://img.youtube.com/vi/e3iG1YwLLdQ/0.jpg)](https://youtu.be/e3iG1YwLLdQ)
3. T - junctions to and fro</br>
[![Watch the video](https://img.youtube.com/vi/7VvkeIZoFew/0.jpg)](https://youtu.be/7VvkeIZoFew)
4. maze solving
5. maze shortest path(mapping)
## Note for assignment 1 and 2:
<img src="https://github.com/skyap/alphabot2/blob/master/images/to.jpg" width="400"></br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/to_and_fro.jpg" width="400"></br>
1. Line tracker sensors return analog readings. You need to convert this to digital for decision making.</br>
2. You need to understand what your sensors' logic in different situation:</br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/logic1.jpg" width="400">

## Note for assignment 3
<img src="https://github.com/skyap/alphabot2/blob/master/images/t-junctions.jpg" width="400"></br>
1. Simple straight line with branches 
2. What your sensors' logic at junction?

## Note and rules for assignment 4 and 5:
1. Simply connected line maze will be used (no loops)
2. Black line on a while or bright background.
3. Each line maze has a start and finish point. The robot is expected to follow the lines and find it's way from start to finish. No mark is giving based on finishing time.
4. 8 maze possibilities
<img src="https://github.com/skyap/alphabot2/blob/master/images/maze1.jpg" width="400">
5. Below will not be implemented
<img src="https://github.com/skyap/alphabot2/blob/master/images/acute_turn.jpg" width="400">
6. line will be at least visible by one sensor all the time</br>
7. This is the examples of line maze(with left hand rule)
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1.jpg" width="400">
8. This is the example of line maze shortest path from start to finish
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1-shorest_path.jpg" width="400">
9. This is the example of line maze shortest path from finish to start 
<img src="https://github.com/skyap/alphabot2/blob/master/images/examplemaze1-shorest_path2.jpg" width="400">


	
	