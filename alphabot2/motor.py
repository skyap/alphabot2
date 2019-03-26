import socket
import struct


class motor:
	def __init__(self,address='192.168.0.116',port=8004):
	
		self.client_socket = socket.socket()
		self.client_socket.connect((address, port))
	def send_one_message(self,data):
		length = len(data)
		self.client_socket.sendall(struct.pack("!I",length))
		self.client_socket.sendall(data.encode("utf-8"))
	def command(self,cmd,speed=None,duration=None):
		# cmd = forward,backward,left,right,set_left_speed,set_right_speed
		# speed = float 
		# duration  = float 
		assert not isinstance(speed,str),"Speed should be an int or float"
		assert not isinstance(duration,str),"Speed should be an int or float"
		if speed != None:
			if speed>100 or speed<0:
				self.send_one_message("stop")
				assert False,"Speed should in between 0 and 100"
		if speed==None and duration==None:
			assert cmd in ["forward","backward","left","right"],"Command with 1 \
				parameter need to be either forward,backward,left,right"
			data=cmd 
		elif duration==None:
			assert cmd in ["set_left_speed","set_right_speed"],"Command with 2 \
				parameters need to be either set_left_speed or set_right_speed"
			data=cmd+" "+str(speed)
		else:
			assert cmd in ["forward","backward","left","right"],"Command with 3 \
				parameter need to be either forward,backward,left,right"
			data=cmd+" "+str(speed)+" "+str(duration)
		self.send_one_message(data)
		
	def stop(self):
		self.client_socket.close()

if __name__=="__main__":
	while True:
		try:
			data = input("command speed duration")
			send_one_message(client_socket,data)
		except KeyboardInterrupt as e:
			print("ERROR: ",e)
			client_socket.close()
			break