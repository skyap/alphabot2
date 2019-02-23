from line_tracker import line_tracker
import time

lt = line_tracker()
lt.start()
max_sensor_values = [0]*5
min_sensor_values = [float('inf')]*5
for i in range(5):
	sensor_values = lt.data
	print(sensor_values)
	for j in range(5):
		min_sensor_values[j]=min(min_sensor_values[j],sensor_values[j])
		max_sensor_values[j]=max(max_sensor_values[j],sensor_values[j])	
	time.sleep(1)

print("min_sensor_values",min_sensor_values)
print("max_sensor_values",max_sensor_values)	
lt.stop()