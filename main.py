#! /usr/bin/env python
from config import CONFIG
from typing import Any
import plate_recognition as plate_recognition
import log_checks 
import time
from robot_interface import move
from robot_interface import is_moving

# for storing images temporary
image_path = "/home/pi/Desktop/image.jpeg"
num_of_packing_spaces = CONFIG["NUMBER_OF_PACKING_SPACES"]

print("starting ...\n")
i = 0
while True:
    if not is_moving():
        print("plate recognition...\n")
        move(False)
        plate_number = Any
        try:
            plate_number = plate_recognition.get_plate_number(image_path)
        except Exception as err:
            continue
        i = i+1
        packing_space_id = i % num_of_packing_spaces
        if packing_space_id == 0:
            packing_space_id = 1
        if not log_checks.log_check(plate_number, packing_space_id):
            continue #repeat the process
        move(True) 
