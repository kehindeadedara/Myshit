import time
import board
import busio
import signal
from time import ctime

import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import sys
import getopt
import logging

def current_time():
    newcur = ctime().split()[:]
    return '-'.join(str(x) for x in newcur)

def interrupt_handler(sig, frame):
    logging.info("Receiving ending")
    sys.stdout.flush()
    sys.exit(0)


def write_file(current_time):
    file_name  = "DataLog/RXDATA/Photodiode{}.log".format(current_time)
    open(file_name, 'w+')
    logging.basicConfig(filename= file_name, level = logging.INFO)

class PhotoSet(object):
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1015(self.i2c)
        self.channel = AnalogIn(self.ads, ADS.P3)

    def input_signal(self):
        return self.channel.value, self.channel.voltage
    
    def signal(self):
        return self.channel.value

    def voltage(self):
        return self.channel.voltage

threshold = 29152
frequency = 30

def usage() -> None:
    print(' <photodiode receivier> -t <threshold>')
    print('-t or --threshol\t: set photodiode threhold')

def convert_analogtoOI(signal, threshold) -> int:
    if signal <= threshold:
        return 0
    else:
        return 1

def main(argv) -> None:
    global threshold, frequency
    print("Receiving photodiode data....")
    write_file(current_time())
    if len(argv) == 1:
        print('Using default values of: A0 threshold')
    try:
        opts, args = getopt.getopt(argv, "ht:", ["threshold="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-t', '--threshold'):
            print("passed..")
            threshold = int(arg)
        elif opt in ('-f', '--frequency'):
            print("passed..")
            frequency = int(arg)

    signal.signal(signal.SIGINT, interrupt_handler)
    diode = PhotoSet()
    while True:
        logging.info('{}'.format(str(diode.signal())))
        time.sleep(1/frequency)


if __name__ == "__main__":
    main(sys.argv[1:])