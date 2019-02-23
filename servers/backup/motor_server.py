import socket
import struct
import time
from AlphaBot2 import AlphaBot2

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

ab = AlphaBot2()
ab.stop()


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8004))
server_socket.listen(0)
connection,address = server_socket.accept()
print("Connect to: ",address)

while True:
	try:
		code = recv_one_message(connection).decode("utf-8")
		command,speed,duration = code.split()
		print(command,speed,duration)
		speed = float(speed)
		duration = float(duration)
		# forward second speed
		# backward second speed 
		# left second speed 
		# right second speed
		ab.PA = speed
		ab.PB = speed 
		if command == "forward":
			ab.forward()
		elif command == "backward":
			ab.backward()
		elif command == "left":
			ab.left()
		elif command == "right":
			ab.right()
			
		time.sleep(duration)
		ab.stop()
		

	except (socket.error,TypeError) as e:
		print("Connection Drop: ", address)
		connection.close()
		ab.stop()
		connection,address = server_socket.accept()
		print("Connect to: ",address)
	except KeyboardInterrupt as e:
		print("ERROR: ",e)
		ab.stop()
		connection.close()
		server_socket.close()

4
	
	
	
