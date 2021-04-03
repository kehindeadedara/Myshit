
import os,sys, signal
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
import time
from time import ctime, sleep

 
# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, baudrate = 256000)
 
# used to scale data to fit on the screen
time = ctime()
cur_file = open('RXDATA/' + time + ".txt", "w+")


def interrupt_handler(sig, frame):
    print("You've pressed Ctrl+C!")
    sys.stdout.flush()
    sys.exit(0)
#change to a Log file!

signal.signal(signal.SIGINT, interrupt_handler)
def main(argv):
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
        print('Stoping.....')
        sys.exit(0)
    
    cur_file.close()
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    sys.exit(0)

if __name__ == "__main__":
    main()

