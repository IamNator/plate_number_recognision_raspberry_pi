from plate_recognition import get_plate_number
from log_checks import log_check 
from robot_interface import move
from robot_interface import is_moving


i = 0
while True:
    if is_moving() == 0:
        move(False)
        plate_number = get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if not log_check(plate_number, packing_space_id):
            continue #repeat the process
        move(True)        