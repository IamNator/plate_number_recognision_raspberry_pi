#!/usr/bin/python3

import os
import sys
import requests
from io import BytesIO
from config import CONFIG
from picamera import PiCamera
from time import sleep
from log_checks import log_check


# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = CONFIG['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = CONFIG['COMPUTER_VISION_ENDPOINT']
ocr_url = endpoint + "/vision/v3.2/ocr?language=unk&detectOrientation=true&model-version=latest"

# takes a picture
def take_picture():
    camera = PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()


def get_plate_number():
    take_picture()
    image_path = "/home/pi/Desktop/image.jpg"
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()

    params = {'language': 'unk', 'detectOrientation': 'true'}
    # Set Content-Type to octet-stream
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    # put the byte array into your post request
    response = requests.post(ocr_url, headers=headers, params=params, data = image_data)
    response.raise_for_status()

    analysis = response.json()


    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)
    word_infos

    plate_number = ""
    for word_info in word_infos:
        plate_number += word_info["text"]
        
    return plate_number




