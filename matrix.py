import time
import busio
import board
import Jetson.GPIO as GPIO
from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)

#color = matrix.Matrix8x8(i2c, 0x72)
#color2 = matrix.Matrix8x8x2(i2c, 0x76)
#color3 = matrix.Matrix8x8x2(i2c, 0x70)
#color4 = matrix.Matrix8x8x2(i2c, 0x71)
#color[6,4] = 1
def perform(color):
   color[2,2] = 1
   color[2,3] = 1
   color[2,4] = 1
   color[2,5] = 1
   color[3,2] = 1
   color[3,3] = 1
   color[3,4] = 1
   color[3,5] = 1
   color[4,2] = 1
   color[4,3] = 1
   color[4,4] = 1
   color[4,5] = 1
   color[5,2] = 1
   color[5,3] = 1
   color[5,4] = 1
   color[5,5] = 1
def color_function(color1,color2, colo3, color4):
    try:
        while True:
            time.sleep(0.5)
            perform(color1)
            perform(color2)
            perform(color3)
            perform(color4)
            color1.show()
            color2.show()
            color3.show()
            color4.show()
            time.sleep(0.5)
            color1.fill(0)
            color2.fill(0)
            color3.fill(0)
            color4.fill(0)
            print("h")
    finally: 
         GPIO.cleanup()
	


color1 = matrix.Matrix8x8(i2c, 0x72)
color2 = matrix.Matrix8x8(i2c, 0x76)
color3 = matrix.Matrix8x8(i2c, 0x70)
color4 = matrix.Matrix8x8(i2c, 0x71)
color_function(color1, color2, color3, color4)
