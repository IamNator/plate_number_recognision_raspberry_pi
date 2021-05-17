import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time
from openalpr import Alpr
import sys
import cv2
from datetime import datetime
import os

button = 2

GPIO.setup(button,GPIO.IN)

# Raspberry Pi pin configuration:
lcd_rs        = 21  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 20
lcd_d4        = 16
lcd_d5        = 12
lcd_d6        = 7
lcd_d7        = 8

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)


plate_detected = False

alpr = Alpr("eu", "/home/pi/openalpr/src/build/config/openalpr.conf", "/home/pi/openalpr/runtime_data")

alpr.set_top_n(20)
alpr.set_default_region("md")

reset = True

while reset == True:
    
    lcd.set_backlight(0)
    lcd.clear()
    print "Automatic Number Plate Detection"
    lcd.message('  Raspberry pi\n     Based     ')
    time.sleep(2)
    lcd.clear()
    lcd.message('Automatic Number\nPlate Detection')
    time.sleep(3)
    
    lcd.clear()
    lcd.message('Searching for\nCamera')
    print "Searching for Camera"
    time.sleep(2)

    camera=cv2.VideoCapture(0)
    
    if not camera.isOpened():
        main = False
        print "can't open the camera"
        lcd.clear()
        lcd.message('Error:Camera not\nFound')
        time.sleep(2)
        lcd.clear()
        lcd.message('Connect Camera &\npress reset')
        while GPIO.input(button) == True:
            None
    
    else:
        main = True
        print "camera found"
        lcd.clear()
        lcd.message('Found Camera')
        time.sleep(2)
            
    while True:

        ret, frame = camera.read()

        results = alpr.recognize_file(frame)
        
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
            lcd.clear()
            lcd.message('license plate \nno. is '+ candidate['plate'] )
            plate_detected = False
        else:
            lcd.clear()
            lcd.message('Plate not detected..')
            
    
        if GPIO.input(button) == False:
            camera.release()
            break


