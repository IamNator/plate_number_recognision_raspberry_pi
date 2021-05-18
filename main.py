from plate_recognition import get_plate_number
from log_checks import log_check 
from robot_interface import move
from robot_interface import is_moving


i = 0
while 1:
    if is_moving() == 0:
        move(false)
        plate_number = get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if log_check(plate_number, packing_space_id) == 0:
            continue #repeat the process
        move(true)        