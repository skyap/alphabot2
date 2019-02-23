import socket
import struct
import RPi.GPIO as GPIO
import time
import threading

def send_one_message(sock,data):
	length = len(data)
	sock.sendall(struct.pack("!I",length))
	sock.sendall(data.encode("utf-8"))
	


class line_tracker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.numSensors = 5
		self.CS = 5
		self.Clock = 25
		self.Address = 24
		self.DataOut = 23
		self.Button = 7

		self.kill = False

	def run(self):		
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.Clock,GPIO.OUT)
		GPIO.setup(self.Address,GPIO.OUT)
		GPIO.setup(self.CS,GPIO.OUT)
		GPIO.setup(self.DataOut,GPIO.IN,GPIO.PUD_UP)
		
		server_socket = socket.socket()
		server_socket.bind(('0.0.0.0', 8006))
		server_socket.listen(0)
		connection,address = server_socket.accept()
		print("Connect to: ",address)
		
		
		while not self.kill:
			try:
					
				data = " ".join(map(str,self.AnalogRead()))
				send_one_message(connection,data)

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
		
	def AnalogRead(self):
		value = [0]*(self.numSensors+1)
		#Read Channel0~channel6 AD value
		for j in range(0,self.numSensors+1):
			GPIO.output(self.CS, GPIO.LOW)
			for i in range(0,4):
				#sent 4-bit Address
				if(((j) >> (3 - i)) & 0x01):
					GPIO.output(self.Address,GPIO.HIGH)
				else:
					GPIO.output(self.Address,GPIO.LOW)
				#read MSB 4-bit data
				value[j] <<= 1
				if(GPIO.input(self.DataOut)):
					value[j] |= 0x01
				GPIO.output(self.Clock,GPIO.HIGH)
				GPIO.output(self.Clock,GPIO.LOW)
			for i in range(0,6):
				#read LSB 8-bit data
				value[j] <<= 1
				if(GPIO.input(self.DataOut)):
					value[j] |= 0x01
				GPIO.output(self.Clock,GPIO.HIGH)
				GPIO.output(self.Clock,GPIO.LOW)
			#no mean ,just delay
#			for i in range(0,6):
#				GPIO.output(self.Clock,GPIO.HIGH)
#				GPIO.output(self.Clock,GPIO.LOW)
			time.sleep(0.0001)
			GPIO.output(self.CS,GPIO.HIGH)
#		print value[1:]
		return value[1:]
		
	def stop(self):
		self.kill = True
		socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect( ("0.0.0.0",8006))
		#server_socket.close()
