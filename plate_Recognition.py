import os
import sys
import requests
# If you are using a Jupyter Notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
from config import CONFIG
from picamera import PiCamera

# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = CONFIG['COMPUTER_VISION_SUBSCRIPTION_KEY']
endpoint = CONFIG['COMPUTER_VISION_ENDPOINT']
ocr_url = endpoint + "vision/v3.1/ocr"

# Read the image into a byte array
camera = PiCamera()
camera = 

ret, frame = camera
image_data = frame

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

# Display the image and overlay it with the extracted text.
plt.figure(figsize=(5, 5))
image = Image.open(BytesIO(requests.get(image_url).content))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3],
                      fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()
plt.axis("off")

    







