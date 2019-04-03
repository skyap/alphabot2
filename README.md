# alphabot2

## About
<img src="https://github.com/skyap/alphabot2/blob/master/images/alphabot2-pizero-8.jpg" width="400"></br>
1. To create a easy to use API for students to interact with alphabot2</br>
2. Students will be focus on the testing of algorithms on the robot instead of dealing with GPIO on Pi.</br>

official webpage:</br>
https://www.waveshare.com/wiki/alphabot2</br>
## Python 3 Installation & Setup Guide
Please follow below link to install Python 3 on your system</br>
<a href="https://github.com/skyap/alphabot2/blob/master/README_python_installation.md" target="_blank">https://github.com/skyap/alphabot2/blob/master/README_python_installation.md</a>
## Install, Upgrade and Uninstall this library
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

## Operating of AlphaBot2-PiZero
1. Power up alphabot2 (USB or batteries)</br>
2. After you hear a beep, the robot is ready to go</br>
3. Use buttons to reboot or safely shutdown AlphaBot2-PiZero</br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/button.png" width="400"></br>

## Examples of Python codes:
<a href="https://github.com/skyap/alphabot2/blob/master/README_examples.md" target="_blank">https://github.com/skyap/alphabot2/blob/master/README_examples.md</a>

## Robot challenges
<a href="https://github.com/skyap/alphabot2/blob/master/README_challenges.md" target="_blank">https://github.com/skyap/alphabot2/blob/master/README_challenges.md</a>

## Robot basic
1. Type of turning</br>
<img src="https://github.com/skyap/alphabot2/blob/master/images/robot_turn.jpg" width="400"></br>
2. Spin turn by setting both wheel speed similiar(plus and minus based on your experience) and send left or right command
3. Pivot turn by setting one wheel speed and send left or right command




	
	