import requests
from config import CONFIG
from datetime import datetime

# log_check(plate_number, packing_space_id, current_time)
def log_check(plate_number, packing_space_id ):
    mawaqif_url = CONFIG["MAWAQIF_UPLOAD_CHECKS"]
    # Set Content-Type to octet-stream
    headers = {'Content-Type': 'application/json'}
    # put the byte array into your post request
    log = {
    "plate_number":plate_number,
    "packing_space_id": packing_space_id,
    "current_time": datetime.now(),
    "is_empty": is_empty(plate_number)}
    
    response = requests.post(mawaqif_url, headers=headers, data = log)
    response.raise_for_status()
    if response.status == 200:
        return True
    return False


def is_empty(plate_number):
    if plate_number == "": 
        return True
    return False