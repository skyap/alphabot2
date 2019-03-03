# AlphaBot2-PiZero
## About

## **_WARNING!!_**
1. Do not run motors when power Pi Zero W from USB</br>
2. When weird behaviours occur, such as below, turn off power and charge your battery:</br>
	2.1. Servo work fine with your code but when you try it later with the same code it didn't work correctly.</br>
	2.2. Conectivity to Pi Zero W suddenly drop.</br>
3. AlpahBot2 have to be on the floor before you run any commands on motors.

## Softwares and libries required
1. python3+ 
2. numpy
3. opencv (not required for the moment)
4. IDE (PyCharm, IDLE, Stani's Python Editor, Spyder, Jupyter Notebook, Notepad, Notepad++, etc.)

## Python resources
if you are new to python, below is the best beginner course for you:</br>
https://www.coursera.org/learn/python

## Program required
1. VNC Viewer(if the Pi running GUI)
2. PuTTY(for window user)/ SSH (for linux user)
3. FileZilla(remote transfer files between pc and pi)

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
2. Unzip the Clients folder

## Step for startup socket server
1. Power up AlphaBot2-PiZero (USB or batteries)
2. Connect to router "Robot", password: 1234567890
2. Look for IP of your robot's name in the _DHCP Client Table_
3. IP: 192.168.1.*
4. Open VNC Viewer
5. Navigate to File > New Connections, type the IP in VNC Server, press OK, double click on the new icon</br></br>
6. <img src="images/vnc1.jpg" width="400"></br>
7. User Name: pi</br>
8. Password: raspberry</br>
9. navigate to Documents > Servers</br> 
10. Tools > Open Current Folder in Terminal</br>
<img src="images/vnc2.jpg" width="400"></br>
11. Modify main.py if you are not going to run all the socket servers
12. Type below in the terminal</br>
	$ python3 main.py

## Step to shutdown socket server
**_CTRL+c_** or **_CTRL+z_**
## Step to shutdown AlphaBot2-PiZero
1. Similiar to how you shutdown Windows
## Step to update file in PiZero
1. To be advice later
## Issues
1. In ad-hoc mode, some time connection establish is not good. If you can't VNC, PuTTY/SSH or FileZilla into Pi after ad-hoc connection, try to disconnect and reconnect again.</br></br>
2. OSError: [Errno 98] Address already in use  
	$ sudo netstat -nlp | grep <800*></br>
	$ sudo kill -9 <process>

## Examples
### <u>line tracker</u>
from line_tracker import line_tracker</br>
address = "192.168.1.104"</br>
lt = line_tracker(address)</br>
lt.start()</br>
print(lt.data)</br>
lt.stop()</br>


### <u>motor</u>
from motor import motor</br>
address = "192.168.1.104"</br>
mot = motor(address)</br>

mot.command("set_left_speed",10)</br>
mot.command("set_right_speed",100)</br>
mot.command("forward")</br>
mot.command("backward")</br>
mot.command("left")</br>
mot.command("right")</br>
mot.command("stop")</br>

mot.stop()</br>






	
	