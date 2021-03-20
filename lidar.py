
import os
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
import time
from time import ctime, sleep

 
# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, baudrate = 256000)
 
# used to scale data to fit on the screen
time = ctime()
cur_file = open(time + ".txt", "w+")

max_distance = 0
try:
    print(lidar.info)

    sleep(10)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
               data = {"angle":angle, "distance":distance, "time": ctime()}
               cur_file.write(str(data) + '\n')
               print("scanning..")
except KeyboardInterrupt:
    print('Stoping.')

cur_file.close()
lidar.stop()
lidar.stop_motor()
lidar.disconnect()

