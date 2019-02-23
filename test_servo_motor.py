from servo import servo
from motor import motor
import time

ser=servo()
mot=motor()
for i in range(0,181):
	ser.horizontal(i)
	time.sleep(1)
ser.horizontal(90)

for i in range(0,110):
	ser.vertical(0)
	time.sleep(1)
ser.vertical(90)

time.sleep(1)

mot.command("forward",10,1)
time.sleep(1)
mot.command("backward",10,1)
time.sleep(1)
mot.command("left",10,1)
time.sleep(1)
mot.command("right",10,1)
time.sleep(1)

mot.stop()
ser.stop()