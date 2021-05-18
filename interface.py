import RPi.GPIO as GPIO
import time
import sys
import cv2
from datetime import datetime
import os

outputPIN = 2
inputPIN = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(outputPIN,GPIO.OUT)
GPIO.setup(inputPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# returns the state of the robot, moving or not
def is_moving():
    if GPIO.input(inputPIN) == GPIO.HIGH
        return true

    return false


# move take a boolean value, it signals if the robot can move or not
def move(state):
    if state
        start_motor
        return
    
    stop_motor
        

def start_motor:
    GPIO.output(outputPIN, GPIO.HIGH)    

def stop_motor:
    GPIO.output(outputPIN, GPIO.LOW)
      


