import time
import busio
import board
import Jetson.GPIO as GPIO
from adafruit_ht16k33 import matrix
from Myshit.MatrixLED.BackMatrix import LEDmatrix

frontled = LEDmatrix(0x71, 0x72)	
frontled.transfer_bit(0.3)