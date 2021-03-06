#!/usr/bin/python3

import os
import sys
import requests
from io import BytesIO
from config import CONFIG
from time import sleep
from log_checks import log_check
from take_picture import take_picture

# uploads a car images (image_date | byte array) to AZURE Car recognition Service and returns the json response
def post_request(image_data):
    
    # Add your Computer Vision subscription key and endpoint to your environment variables.
    subscription_key = CONFIG['COMPUTER_VISION_SUBSCRIPTION_KEY']
    ocr_url_endpoint = CONFIG['COMPUTER_VISION_ENDPOINT']
     
   
    params = {'language': 'unk', 'detectOrientation': 'true'}
    # Set Content-Type to octet-stream
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    # put the byte array into your post request
    try:
        response = requests.post(ocr_url_endpoint, headers=headers, params=params, data = image_data)
        response.raise_for_status()
    except Exception as er:
        print(er)
        print(response.json())
    else:
        return response.json()
        

# extracts car image from image_path and returns the plate_number
def get_plate_number(image_path):
   
    # Read the image into a byte array s
    image_data = open(image_path, "rb").read()
    analysis = post_request(image_data)
   
    
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
