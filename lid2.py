import os
from math import cos, sin, pi, floor
import pygame
from adafruit_rplidar import RPLidar
 

 
# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME)
 
# used to scale data to fit on the screen
max_distance = 0
try:
    print(lidar.info)
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        print(scan_data)
 
except KeyboardInterrupt:
    print('Stoping.')

lidar.stop()
lidar.disconnect()
