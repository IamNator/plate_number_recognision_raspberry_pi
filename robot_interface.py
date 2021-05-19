import RPi.GPIO as GPIO
from datetime import time

outputPIN = 3
inputPIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPIN, GPIO.OUT)
GPIO.setup(inputPIN, GPIO.IN)


# returns the state of the robot, moving or not
def is_moving():
    if GPIO.input(inputPIN) == GPIO.HIGH:
        return 1

    return 0


# move take a boolean value, it signals if the robot can move or not
def move(state):
    if state:
        start_motor
        return
    
    stop_motor
        

def start_motor():
    GPIO.output(outputPIN, GPIO.HIGH)    

def stop_motor():
    GPIO.output(outputPIN, GPIO.LOW)
      


