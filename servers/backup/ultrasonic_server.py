import socket
import struct
import time
import RPi.GPIO as GPIO

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

def dist():
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	#time.sleep(0.00001)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*340000/2

def send_one_message(sock,data):
	length = len(data)
	sock.sendall(struct.pack("!I",length))
	sock.sendall(data.encode("utf-8"))
	
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8001))
server_socket.listen(0)
connection,address = server_socket.accept()
print("Connect to: ",address)
while True:
	try:	
		send_one_message(connection,str(dist()))
		time.sleep(0.1)
		
	except socket.error as e:
		print("Connection Drop: ", address)
		connection,address = server_socket.accept()
		print("Connect to: ",address)
	except KeyboardInterrupt as e:
		print("ERROR: ",e)
		connection.close()
		server_socket.close()