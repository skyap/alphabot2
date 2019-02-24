# AlphaBot2-PiZero

## Warning
1. Do not run motors when power Pi Zero W from USB</br>
2. When weird behaviours occur, such as below, turn off power and charge your battery:</br>
	2.1. Servo work fine with your code but when you try it later with the same code it didn't work correctly.</br>
	2.2. Conectivity to Pi Zero W suddenly drop.</br>

## Softwares and libries required
1. python3+
2. numpy
3. opencv

## Program required
1. VNC Viewer(if the Pi running GUI)
2. PuTTY(for window user)/ SSH (for linux user)
3. FileZilla(remote transfer files between pc and pi)

## Issues
1. In ad-hoc mode, some time connection establish is not good. If you can't VNC, PuTTY/SSH or FileZilla into Pi after ad-hoc connection, try to disconnect and reconnect again.
2. OSError: [Errno 98] Address already in use
	$ sudo netstat -nlp |grep 8000
	$ sudo kill -9 <process>

## Step
1. Power up AlphaBot2-PiZero (USB or batteries)
2. IP: 192.168.1.1 Port: 22
3. User Name/ Password: to be inform in class
4. navigate to Documents
	$ cd Documents
	$ cd servers
	$ python3 
	
5. To shutdown
	$ sudo shutdown -h now
	
	