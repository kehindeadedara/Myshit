from datetime import *
import signal
import sys
import time
import logging
import getopt
import random
import subprocess
from main_matrix import LEDmatrix
#from car_config import Config
from tqdm import tqdm

#config_files = Config().dict

try:
    #matrix = LEDmatrix(config_files['front_led_address'][0], config_files['front_led_address'][1])
    matrix = LEDmatrix(0x70, 0x76)
    matrix.transfer_bit(0)
except:
    print('Something went wrong in the front led script!')
    sys.exit(0)



frequency = 30  # effectively a 30Hz transmission rate
message = 'HelloWorld'
times = 10
# variables for perma state transmission
state_flag = False
random_size = 500



def interrupt_handler(sig, frame):
    print("You've pressed Ctrl+C!")
    GPIO.cleanup()
    sys.stdout.flush()
    sys.exit(0)


def create_transmission(bitstream, times_to_multiply):
    return bitstream * times_to_multiply  # multiplies it by the number of times to be repeated


def transmit(transmission_bits):
    try:
        for bit in tqdm(transmission_bits, desc= 'back_transmitter:'):
            matrix.transfer_bit(int(bit))
            time.sleep(1/frequency)
    finally:
        GPIO.cleanup()
        sys.exit()

def generate_random_bitstream(size):
    bitstream = ""
    for i in range(size):
        bitstream += str(random.randint(0, 1))

    return bitstream


def usage():
    print('transmitter_randombits_repeat.py -s <define_static_state> -r <length_of_random_bitstream> -f '
          '<frequency_to_transmit> -t <number_of_times>')
    print('-f or --frequency\t: Frequency to transmit at')
    print('-r or --random\t: Flag to set random bit transmission followed by the size of the bitstream')
    print('-t or --times\t: Number of times the random bitstream is to be repeated')


def generate_random_bitstream(size):
    bitstream = ""
    for i in range(size):
        bitstream += str(random.randint(0, 1))
    return bitstream


def main(argv):
    global output_pin, frequency, state_flag, random_flag, random_size, times
    if len(argv) == 1:
        print('Using default values of: Output Pin = Board 12, Frequency = 30 Hz')
    try:
        opts, args = getopt.getopt(argv, "hf:r:t:", ["freq=", "random=", "times="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-f', '--freq'):
            frequency = int(arg)
        elif opt in ('-r', '--random'):
            random_flag = True
            random_size = int(arg)
        elif opt in ('-t', '--times'):
            times = int(arg)
    
    signal.signal(signal.SIGINT, interrupt_handler)

    try:
        random_bits = generate_random_bitstream(random_size)
        transmission = create_transmission(random_bits, times)
        #subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE)
        #subprocess.Popen(['python3', 'Transmitter/blink.py'])
        transmit(transmission)
        print('transmission completed....')
    except:        
        print('No flags set, exiting')
        usage()
        matrix.transfer_bit(0)
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
