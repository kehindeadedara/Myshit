import os,sys, signal
from math import cos, sin, pi, floor
from adafruit_rplidar import RPLidar
import time
from time import ctime, sleep
from car_config import Config
import logging

config_file = Config().dict
 
# Setup the RPLidar
PORT_NAME = config_file['lidar_port']
time = ctime()
#cur_file = open('RXDATA/' + time + ".txt", "w+")


def interrupt_handler(sig, frame):
    print("You've pressed Ctrl+C!")
    sys.stdout.flush()
    sys.exit(0)
#change to a Log file!


def main():
    signal.signal(signal.SIGINT, interrupt_handler)
    lidar = RPLidar(None, PORT_NAME, baudrate = 256000)
    logging.basicConfig(filename="Datalog/Receiver/lidar_data_{}.log".format(time), level = logging.INFO)
    max_distance = 0
    try:
        logging.info("Starting scanning>>>")
        logging.info(lidar.info)
        sleep(10)
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                data = {"angle":angle, "distance":distance, "time": ctime()}
                logging.info(str(data))
    except KeyboardInterrupt:
        logging.info("Stop scanning")
        sys.exit(0)
    
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    sys.exit(0)

if __name__ == "__main__":
    main()
