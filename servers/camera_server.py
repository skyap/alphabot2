import io
import socket
import struct
import time
import picamera
import threading

class camera(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.kill = False
	def run(self):
		server_socket = socket.socket()
		server_socket.bind(('0.0.0.0', 8000))
		server_socket.listen(0)
		connection,address = server_socket.accept()
		connection = connection.makefile('wb')
		print("Connect to: ",address)
		while not self.kill:
			try:
				with picamera.PiCamera() as camera:
					camera.resolution = (640, 480)
					camera.framerate = 30
					camera.rotation = 180
					#camera.start_preview()
					#time.sleep(2)
					stream = io.BytesIO()
					for foo in camera.capture_continuous(stream, 'jpeg',use_video_port=True):
						connection.write(struct.pack('<L', stream.tell()))
						connection.flush()
						stream.seek(0)
						connection.write(stream.read())
						stream.seek(0)
						stream.truncate()
				connection.write(struct.pack('<L', 0))
				print("running")
			except socket.error as e:
				print("Connection Drop: ", address)
				connection,address = server_socket.accept()
				connection = connection.makefile('wb')
				print("Connect to: ",address)
			except KeyboardInterrupt as e:
				print("ERROR: ",e)
				connection.close()
		connection.close()
		server_socket.close()
	def stop(self):
		self.kill = True
		socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect( ("0.0.0.0",8000))
		#server_socket.close()
if __name__=="__main__":
	a=camera()
	a.start()
	while True:
		try:
			time.sleep(100)
		except KeyboardInterrupt:
			a.stop()
			break
	
