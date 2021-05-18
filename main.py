from plate_recognition import get_plate_number 
from log_checks import log_check 
import interface as interface
# from interface import is_moving 





i = 0
while true:
    if interface.is_moving() == false:
        interface.move(false)
        plate_number = get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if log_check(plate_number, packing_space_id) == false:
            continue #repeat the process
        interface.move(true)        