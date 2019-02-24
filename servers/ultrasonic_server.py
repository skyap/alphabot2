import socket
import struct
import time
import RPi.GPIO as GPIO
import threading







def send_one_message(sock,data):
	length = len(data)
	sock.sendall(struct.pack("!I",length))
	sock.sendall(data.encode("utf-8"))

class ultrasonic(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.kill = False
		self.TRIG = 22
		self.ECHO = 27

	def dist(self):
		GPIO.output(self.TRIG,GPIO.HIGH)
		time.sleep(0.000015)
		#time.sleep(0.00001)
		GPIO.output(self.TRIG,GPIO.LOW)
		t1 = time.time()
		while not GPIO.input(self.ECHO):
			if time.time() - t1>0.002:
				break
		t1 = time.time()
		while GPIO.input(self.ECHO):
			if time.time() - t1>0.002:
				break
			
		t2 = time.time()
		return (t2-t1)*340000/2

	def run(self):	
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.TRIG,GPIO.OUT,initial=GPIO.LOW)
		GPIO.setup(self.ECHO,GPIO.IN)

		server_socket = socket.socket()
		server_socket.bind(('0.0.0.0', 8001))
		server_socket.listen(0)
		connection,address = server_socket.accept()
		print("Connect to: ",address)
		while not self.kill:
			try:	
				data = str(self.dist())
				send_one_message(connection,data)
				time.sleep(0.01)
				
			except socket.error as e:
				print("Connection Drop Ultrasonic: ", address)
				connection,address = server_socket.accept()
				print("Connect to: ",address)
			except KeyboardInterrupt as e:
				print("ERROR: ",e)
				connection.close()
				server_socket.close()
				GPIO.cleanup()
		connection.close()
		server_socket.close()
		GPIO.cleanup()
	def stop(self):
		self.kill = True
		socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect( ("0.0.0.0",8001))
		#server_socket.close()