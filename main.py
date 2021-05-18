import get_plate_number from plate_recognition
import log_check from log_checks
import move from interface
import is_moving from interface





i = 0
while true:
    if !is_moving():
        move(false)
        plate_number = get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if !log_check(plate_number, packing_space_id)
            continue #repeat the process
        move(true)        