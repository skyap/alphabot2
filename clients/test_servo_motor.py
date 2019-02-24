# from servo import servo
from motor import motor
import time

# ser=servo()

# for i in range(0,181):
	# ser.horizontal(i)
	# time.sleep(1)
# ser.horizontal(90)

# for i in range(0,110):
	# ser.vertical(0)
	# time.sleep(1)
# ser.vertical(90)

# time.sleep(1)


# ser.stop()

mot=motor()
# mot.command("forward",10,2)
# mot.command("backward",10,2)
# mot.command("left",10,2)
# mot.command("right",10,2)

mot.command("set_left_speed",10)
mot.command("set_right_speed",100)
mot.command("forward")

time.sleep(5)
# mot.command("backward")
# time.sleep(10)

mot.stop()