#! /usr/bin/env python
from config import CONFIG
import plate_recognition as plate_recognition
import log_checks 
import time
from robot_interface import move
from robot_interface import is_moving
import threading

# for storing images temporary
image_path = "/home/pi/Desktop/image.jpeg"
num_of_packing_spaces = CONFIG["NUMBER_OF_PACKING_SPACES"]

isMove = False

def check_move():
    isMove = is_moving()
    
t = threading.Timer(0.1, check_move)
    

print("starting ...\n")
i = 0
while True:
    isMove = is_moving()
    while not isMove:
        # isMove = is_moving()
        move(False)
        time.sleep(1)
        
        print("plate recognition...\n")
       
        plate_number = ""
        try:
            plate_number = plate_recognition.get_plate_number(image_path)
        except Exception as err:
            continue
        else:
            i = i+1   
            packing_space_id = i % num_of_packing_spaces
            if packing_space_id == 0:
                packing_space_id = 1
            try:
                is_log_uploaded = log_checks.log_check(plate_number, packing_space_id)
            except Exception as er:
                continue
            else:
                if not is_log_uploaded:
                    continue #repeat the process
            move(True)
            time.sleep(1)
