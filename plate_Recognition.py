import os
import sys
import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# from PIL import Image
from io import BytesIO
from config import CONFIG
from picamera import PiCamera
from time import sleep

# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = CONFIG['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = CONFIG['COMPUTER_VISION_ENDPOINT']
ocr_url = endpoint + "vision/v3.1/ocr"

# Read the image into a byte array
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()


image_path = "/home/pi/Desktop/image.jpg"
# Read the image into a byte array
image_data = open(image_path, "rb").read()

params = {'language': 'unk', 'detectOrientation': 'true'}
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
# put the byte array into your post request
analysis = requests.post(ocr_url, headers=headers, params=params, data = image_data)


# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
word_infos


print(word_infos)



