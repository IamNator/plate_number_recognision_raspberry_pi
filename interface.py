import RPi.GPIO as GPIO
import time
import sys
import cv2
from datetime import datetime
import os

button = 2

GPIO.setup(button,GPIO.IN)


plate_detected = False

alpr = Alpr("eu", "/home/pi/openalpr/src/build/config/openalpr.conf", "/home/pi/openalpr/runtime_data")

alpr.set_top_n(20)
alpr.set_default_region("md")

reset = True

while reset == True:
    
    time.sleep(2)
    camera=cv2.VideoCapture(0)
    
    if not camera.isOpened():
        main = False
        print ("can't open the camera")
        while GPIO.input(button) == True:
            None
    
    else:
        main = True
        print("camera found")
        time.sleep(2)
            
    while True:

        ret, frame = camera.read()

        results = frame
        
        i = 0
        for plate in results['results']:
            i += 1
            for candidate in plate['candidates']:
                prefix = "-"
                if candidate['matches_template']:
                    prefix = "*"

                plate_detected = True
                break

        if plate_detected:
            print('license plate \nno. is '+ candidate['plate'] )
            plate_detected = False
        else:
            print('Plate not detected..')
            
    
        if GPIO.input(button) == False:
            camera.release()
            break


