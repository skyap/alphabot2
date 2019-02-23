import socket
import struct
import time
from PCA9685 import PCA9685

def recvall(sock,count):
	buf = b''
	while count:
		newbuf = sock.recv(count)
		if not newbuf: 
			return None
		buf += newbuf
		count -= len(newbuf)
	return buf
	
def recv_one_message(sock):
	lengthbuf = recvall(sock,4)
	length, = struct.unpack('!I', lengthbuf)
	return recvall(sock,length)

pwm =PCA9685(0x40)
pwm.setPWMFreq(50)

HPulse= 1600
pwm.setServoPulse(0,HPulse)

VPulse = 1500
pwm.setServoPulse(1,VPulse)



server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8003))
server_socket.listen(0)
connection,address = server_socket.accept()
print("Connect to: ",address)

while True:
	try:
		data = recv_one_message(connection)
		channel,degree = map(int,data.split())
		if channel == 0:
			pulse = degree*2200/180+500
		else:
			pulse = degree*2000/180+500
		pwm.setServoPulse(channel,pulse)
		time.sleep(0.1)
	except (socket.error,TypeError) as e:
		print("Connection Drop: ", address)
		connection.close()
		pwm.setServoPulse(0,1600)
		pwm.setServoPulse(1,1500)
		connection,address = server_socket.accept()
		print("Connect to: ",address)
	except KeyboardInterrupt as e:
		print("ERROR: ",e)
		connection.close()
		server_socket.close()

4
	
	
	
