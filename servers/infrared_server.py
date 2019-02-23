import socket
import struct
import RPi.GPIO as GPIO
import time
import threading

def send_one_message(sock,data):
	length = len(data)
	sock.sendall(struct.pack("!I",length))
	sock.sendall(data.encode("utf-8"))
class infrared(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.kill = False
	def run(self):
		DR = 16
		DL = 19
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
		GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)
		
		server_socket = socket.socket()
		server_socket.bind(('0.0.0.0', 8002))
		server_socket.listen(0)
		connection,address = server_socket.accept()
		print("Connect to: ",address)
		
		
		while not self.kill:
			try:
				DR_status = GPIO.input(DR)
				DL_status = GPIO.input(DL)
				data = str(DR_status)+" "+str(DL_status)
				send_one_message(connection,data)
				time.sleep(0.1)
			except socket.error as e:
				print("Connection Drop: ", address)
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
		socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect( ("0.0.0.0",8002))
		#server_socket.close()
