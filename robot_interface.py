import RPi.GPIO as GPIO
from datetime import time

outputPIN = 16
inputPIN = 18

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outputPIN, GPIO.OUT)
GPIO.setup(inputPIN, GPIO.IN)


# returns the state of the robot, moving or not
def is_moving():
    if GPIO.input(inputPIN) == GPIO.HIGH:
        return True

    return False


# move take a boolean value, it signals if the robot can move or  not
def move(state):
    if state:
        start_motor()
        return
    
    stop_motor()
        

def start_motor():
    GPIO.output(outputPIN, GPIO.HIGH)    

def stop_motor():
    GPIO.output(outputPIN, GPIO.LOW)
      

