#! /usr/bin/env python

import plate_recognition as plate_recognition
import log_checks 
import time
from robot_interface import move
from robot_interface import is_moving

# for storing images temporary
image_path = "/home/pi/Desktop/image.jpeg"

print("starting ...\n")
i = 0
while True:
    if not is_moving():
        print("plate recognition...\n")
        move(False)
        plate_number = plate_recognition.get_plate_number(image_path)
        i = i+1
        packing_space_id = i % 5
        if packing_space_id == 0:
            packing_space_id = 1
        if not log_checks.log_check(plate_number, packing_space_id):
            continue #repeat the process
        move(True) 
