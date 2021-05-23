# plate_number_recognision_raspberry_pi
This software tracks cars in a parking lot. This makes detection of defaulter (illegal parking) easy.  

# how?
This software runs on a raspberry pi, it detects a car plates number using a pi camera and sends it to a backend server. This is part of a larger system.

# details
It all starts in the main.py

upon a reception of a signal, the pi sends another signal to signal it's busy (stopping the robot) then takes a picture of a car showing the plate number, the plate number is uploaded to Azure Cognitive Vision API to extract the plate number, the extracted plate number (if any) is sent to a backend server with the packing lot id and current time. At the end of this event, the pi sends another signal to tell the rest of the system it's no longer busy.

Below is a pseudo code of what happens
```
  check for signal (to take pictures) periodically, if none, wait
  if signal is detected then send another to stop the robot, take a picture 
  send picture to Azure Cognitive Vision to extract plate number
  Send plate number, packing lot id and current time to back end server
  repeat the whole process
```

