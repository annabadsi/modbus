import RPi.GPIO as GPIO
import time

ledPin = 12

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)