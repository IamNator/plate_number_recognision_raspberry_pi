import plate_recognition as plate_recognition
import log_checks 
from robot_interface import move
from robot_interface import is_moving


print("starting ...\n")
i = 0
while True:
    if is_moving() == 0:
        print("plate recognition...\n")
        move(False)
        plate_number = plate_recognition.get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if not log_checks.log_check(plate_number, packing_space_id):
            continue #repeat the process
        move(True) 
    