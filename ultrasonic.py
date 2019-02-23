import io
import socket
import struct
from threading import Thread,Event
import time

class ultrasonic:
	def __init__(self,address='192.168.0.116',port=8001):
		self.client_socket = socket.socket()
		self.client_socket.connect((address,port))
		self.data=0
		self.measurement = 0
		self.thread = Thread(target=self._start)
		self.thread.deamon=True
		self.event=Event()
		
		self.kill = False
		
	def recvall(self, count):
		buf = b''
		while count:
			newbuf = self.client_socket.recv(count)
			if not newbuf: 
				return None
			buf += newbuf
			count -= len(newbuf)
		return buf
		
	def recv_one_message(self):
		lengthbuf = self.recvall(4)
		length, = struct.unpack('!I', lengthbuf)
		return self.recvall(length)
		
	def _start(self):
		while not self.kill:		
			self.data = self.recv_one_message().decode("utf-8")
			self.measurement = float(self.data)
			time.sleep(0.001)
		self.client_socket.close()
			
	def start(self):	
		self.thread.start()			

	def stop(self):
		self.kill = True
		
if __name__	== "__main__":		
	a=ultrasonic()
	a.start()
	while True:
		try:
			print(a.data)
			time.sleep(1)
		except KeyboardInterrupt:
			a.stop()
			break
	a.stop()
		
	
