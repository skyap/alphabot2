import io
import socket
import struct
import cv2
import numpy as np 
from threading import Thread,Event

class camera:
	def __init__(self,address='192.168.0.116',port=8000):
		self.client_socket = socket.socket()
		self.client_socket.connect((address,port))
		self.connection = self.client_socket.makefile('rb')
		self.image=[]
		self.thread = Thread(target=self._start)
		self.thread.deamon=True
		self.event=Event()
		
	def _start(self):
		while not self.event.is_set():		
			image_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
			if not image_len:
				break
			image_stream = io.BytesIO()
			image_stream.write(self.connection.read(image_len))
			image_stream.seek(0)			
			self.image = cv2.imdecode(np.fromstring(image_stream.read(),np.uint8),1)
		self.connection.close()
		self.client_socket.close()
			
	def start(self):	
		self.thread.start()			

	def stop(self):
		self.event.set()
		
if __name__=="__main__":
	a=camera('192.168.1.1')
	a.start()
	while True:
		try:
			if a.image!=[]:
				cv2.imshow("image",a.image)
				cv2.waitKey(1)
				
		except KeyboardInterrupt:
			a.stop()
			cv2.destroyAllWindows()
			break	