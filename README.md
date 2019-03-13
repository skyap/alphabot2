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
4. Do not turn the servo with hand, before and after start main.py. It will break the servo. Refer to <a href="https://arduino.stackexchange.com/questions/4076/what-is-commonly-done-to-stop-a-servo-after-reaching-desired-position">what is commonly done to stop a servo after reaching desired position</br></br>
"**_A servo is always running. In a general sense, the servo is a control loop that takes as input a position target and applies force to hold at the requested target._**"


## Softwares and libries required
1. python3+ 
2. numpy (not required for the moment)
3. opencv (not required for the moment)
4. IDE (PyCharm, IDLE, Stani's Python Editor, Spyder, Jupyter Notebook, Notepad, Notepad++, etc.)

## Python resources
if you are new to python, below is the best beginner course for you:</br>
https://www.coursera.org/learn/python

## Program required
1. VNC Viewer(if the Pi running GUI)</br>
2. PuTTY(for window user)/ SSH (for linux user)</br>


## Router settings for PiZero W
1. Use WPA or WPA2 only
2. Ensure it is 2.4GHz

## Step for connect to another WIFI
$ cd /etc/wpa_supplicant</br>
$ sudo nano wpa_supplicant.conf</br>
put below in the the file:</br></br>
network={</br>
&nbsp; &nbsp; &nbsp; &nbsp;ssid="Robot"</br>
&nbsp; &nbsp; &nbsp; &nbsp;psk="1234567890"</br>
&nbsp; &nbsp; &nbsp; &nbsp;priority=1</br>
&nbsp; &nbsp; &nbsp; &nbsp;scan_ssid=1</br>
}</br>

change the **_ssid_** and **_psk_** to your router id and password</br>
after finish press **CTRL+x**, **y**, **ENTER**
## Before start
1. Download latest repository from https://github.com/skyap/AlphaBot2-PiZero
    * on AlphaBot2-PiZero or laptop, open terminal and type:</br>
	$ git clone https://github.com/skyap/AlphaBot2-PiZero
2. Alternatively , downlaod and unzip the folder

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
	$ python3 main.py

## Step to shutdown socket server
**_CTRL+c_** or **_CTRL+z_**
## Step to shutdown AlphaBot2-PiZero
1. Similiar to how you shutdown Windows

## Issues
1. In ad-hoc mode, some time connection establish is not good. If you can't VNC, PuTTY/SSH or FileZilla into Pi after ad-hoc connection, try to disconnect and reconnect again.</br></br>
2. OSError: [Errno 98] Address already in use  
	$ sudo netstat -nlp | grep 8000</br>
	$ sudo kill -9 123

## Examples
### <u>line tracker</u>
from line_tracker import line_tracker</br>
import time</br>
address = "192.168.1.104"</br>
lt = line_tracker(address)</br>
lt.start()</br>
for i in range(100):</br>
&nbsp; &nbsp; &nbsp; &nbsp;# stop for one second</br>
&nbsp; &nbsp; &nbsp; &nbsp;time.sleep(1)</br>
&nbsp; &nbsp; &nbsp; &nbsp;if lt.data==0:</br>
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;continue</br>
&nbsp; &nbsp; &nbsp; &nbsp;print(lt.data)</br>
lt.stop()</br>


### <u>motor</u>
from motor import motor</br>
import time</br>
address = "192.168.1.104"</br>
mot = motor(address)</br>

&#35; mot.command(direction,speed,duration)</br>
&#35; parameters: </br>
&#35; &nbsp; &nbsp; &nbsp; &nbsp;direction: "forward","backward","left","right","set_left_speed","set_right_speed","stop"</br>
&#35; &nbsp; &nbsp; &nbsp; &nbsp;speed: 0-100</br>
&#35; &nbsp; &nbsp; &nbsp; &nbsp;duration: second</br>

mot.command("forward",20,5)</br>
mot.command("set_left_speed",10)</br>
mot.command("set_right_speed",10)</br>
mot.command("forward")</br>
time.sleep(5)</br>
mot.command("stop")</br>
time.sleep(1)</br>
mot.command("backward")</br>
time.sleep(5)</br>
mot.command("stop")</br>
time.sleep(1)</br>
mot.command("left")</br>
time.sleep(5)</br>
mot.command("stop")</br>
time.sleep(1)</br>
mot.command("right")</br>
time.sleep(5)</br>
mot.command("stop")</br>

&#35; stop the motor client socket</br>
mot.stop()</br>






	
	