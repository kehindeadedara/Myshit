import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin = 18

GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)

try:
   while True:
       value = GPIO.HIGH
       GPIO.output(pin,value)
       time.sleep(5)
       value=GPIO.LOW
       print("low")
       GPIO.output(pin, value)
       time.sleep(5)
       print("high")

finally:
    GPIO.cleanup(pin)


