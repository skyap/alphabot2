import io
import socket
import struct
from threading import Thread,Event
import time

class infrared:
	def __init__(self,address='192.168.0.116',port=8002):
		self.client_socket = socket.socket()
		self.client_socket.connect((address,port))
		self.data=0
		self.left=0
		self.right=0
		self.thread = Thread(target=self._start)
		self.thread.deamon=True
		self.event=Event()
		
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
		while not self.event.is_set():		
			self.data = self.recv_one_message().decode("utf-8")
			self.left,self.right = map(int,self.data.split())			
		self.client_socket.close()
			
	def start(self):	
		self.thread.start()			

	def stop(self):
		self.event.set()
		
if __name__	== "__main__":		
	a=infrared()
	a.start()
	while True:
		try:
			print(a.data)
			time.sleep(1)
		except KeyboardInterrupt:
			break
	a.stop()
		
	
