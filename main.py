import plate_recognition
import log_checks
import interface





i = 0
while true:
    if !interface.is_moving():
        move(false)
        plate_number = interface.get_plate_number()
        packing_space_id = i % 4
        i = i+1
        if !log_checks(plate_number, packing_space_id)
            continue #repeat the process
        move(true)        