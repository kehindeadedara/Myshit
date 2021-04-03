import Jetson.GPIO as GPIO
import time
import sys
import getopt
from tqdm.auto import tqdm
import signal

# Pin Definitions
output_pin = 12  # BOARD pin 12
frequency = 1


def interrupt_handler(sig, frame):
    print("You've pressed Ctrl+C!")
    logging.info("Program ending")
    GPIO.cleanup(output_pin)
    sys.exit(0)


def usage():
    print('gpio_blink.py -f <frequency> -p <output_pin>')
    print('-f or --frequency\t: Frequency to toggle between high and low')
    print('-p or --pin\t: The board pin to output the transmission to')


def main(argv):
    global output_pin, frequency
    signal.signal(signal.SIGINT, interrupt_handler)

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        for i in tqdm(range(20), position = 1, leave = True, ascii = False, desc = 'Main LED:'):
            time.sleep((1/frequency))
            # Toggle the output every second
            #print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
    finally: 
        GPIO.output(output_pin, GPIO.LOW)
        GPIO.cleanup()

if __name__ == '__main__':
    main(sys.argv[1:])

