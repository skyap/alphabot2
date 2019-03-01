# AlphaBot2-PiZero
## About

## Warning
1. Do not run motors when power Pi Zero W from USB</br>
2. When weird behaviours occur, such as below, turn off power and charge your battery:</br>
	2.1. Servo work fine with your code but when you try it later with the same code it didn't work correctly.</br>
	2.2. Conectivity to Pi Zero W suddenly drop.</br>

## Softwares and libries required
1. python3+ 
2. numpy
3. opencv (not required for the moments)
4. IDE (PyCharm, IDLE, Stani's Python Editor, Spyder, Jupyter Notebook, Notepad, Notepad++, etc.)

## Python resources
if you are new to python, below is the best beginner course for you:</br>
https://www.coursera.org/learn/python

## Program required
1. VNC Viewer(if the Pi running GUI)
2. PuTTY(for window user)/ SSH (for linux user)
3. FileZilla(remote transfer files between pc and pi)

## Step for startup(router)
1. Power up AlphaBot2-PiZero (USB or batteries)
2. Look for IP in the _DHCP Client Table_
3. Use this IP for communicating with your AlphaBot2-PiZero.

## Issues
1. In ad-hoc mode, some time connection establish is not good. If you can't VNC, PuTTY/SSH or FileZilla into Pi after ad-hoc connection, try to disconnect and reconnect again.</br></br>
2. OSError: [Errno 98] Address already in use  
	$ sudo netstat -nlp | grep <8000></br>
	$ sudo kill -9 <process>

## Step for change from WIFI to ad-hoc and vice versa
1. go to _Desktop_
2. to change to ad-hoc:</br>
$ ./to_adhoc.sh  
3. to change to wifi:</br>
$ ./to_wifi.sh

## Step for startup(ad-hoc)
1. Power up AlphaBot2-PiZero (USB or batteries)
2. IP: 192.168.1.1 Port: 22
3. User Name/ Password: to be inform in class
4. navigate to Documents  
	$ cd Documents
	$ cd servers
	$ python3 
	
5. To shutdown  
	$ sudo shutdown -h now
6. To reboot  
	$ sudo reboot -h now
## Router settings for PiZero W
1. Use WPA or WPA2 only
2. Ensure it is 2.4GHz
## Step for connect to another WIFI
$ cd /etc/wpa_supplicant</br>
$ sudo nano wpa_supplicant.conf</br>
change the **_ssid_** and **_psk_** to your router id and password</br>
after finish press **CTRL+x**, **y**, **ENTER**

## Examples


	
	