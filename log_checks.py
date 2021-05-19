from typing import Any
import requests
import json
from config import CONFIG
from datetime import datetime

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

def is_empty(plate_number):
    if plate_number == "": 
        return True
    return False

# log_check(plate_number, packing_space_id, current_time)
def log_check(plate_number, packing_space_id ):
    mawaqif_url = CONFIG["MAWAQIF_UPLOAD_CHECKS"]
    # Set Content-Type to octet-stream
    headers = {'Content-Type': 'application/json'}
    # put the byte array into your post request
    isEmpty = is_empty(plate_number)
    time_of_check = default
    
    checks_log = {}
    checks_log["plate_number"] = plate_number
    checks_log["packing_space_id"] = packing_space_id
    checks_log["current_time"] = time_of_check
    checks_log["is_empty"] = isEmpty
    
    jsonlog = Any
    
    try:
        jsonlog = json.dumps(checks_log)
    except Exception as er:
        print(er)


    
    try:
        response = requests.post(mawaqif_url, headers=headers, data = jsonlog)
        response.raise_for_status()
    except Exception as er:
        print(er)
        print(response.json())
    else: 
        if response.status_code is 201:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            return True
        else: 
            return False
  

print(log_check("56_FG_O", 2))



