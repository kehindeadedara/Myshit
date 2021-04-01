import time
import busio
import board
import Jetson.GPIO as GPIO
from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)


def perform(color):
    for i in range(1,9):
        for j in range(1,9):
              if i%2 or j%2== 0:
                  pass
              else:
                  color[i,j] = 1


color3 = matrix.Matrix8x8(i2c, 0x70)
color4 = matrix.Matrix8x8(i2c, 0x71)