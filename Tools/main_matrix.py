import time
import busio
import board
import Jetson.GPIO as GPIO
from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)

class LEDmatrix():
    def __init__(self, address1, address2):
        self.left = matrix.Matrix8x8(i2c, address1)
        self.right = matrix.Matrix8x8(i2c, address2)
        
    def high(self, color):
        for i in range(1,9):
            for j in range(1,9):
                if i%2 or j%2== 0:
                    pass
                else:
                    color[i,j] = 1
                    color.show()

    def low(self, color):
        for i in range(1,9):
            for j in range(1,9):
                if i%2 or j%2== 0:
                    pass
                else:
                    color[i,j] = 0
                    color.show()

    def transfer_bit(self, bit):
        if bit == 1:
            self.high(self.left)
            self.high(self.right)
        else:
            self.left.fill(0)
            self.right.fill(0)
        # try:
        #     while True:
        #         time.sleep(frequency)
        #         self.high(self.left)
        #         self.high(self.right)
        #         time.sleep(frequency)
        #         self.left.fill(0)
        #         self.right.fill(0)
        #         # self.low(self.left)
        #         # self.low(self.high)
        # finally:
        #     self.low(self.left)
        #     self.low(self.high)
        #     GPIO.cleanup()
