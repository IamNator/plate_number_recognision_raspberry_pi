from picamera import PiCamera
from time import sleep


# takes a picture
def take_picture(image_path):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # warm up camera
    sleep(1)
    camera.capture(image_path)
    camera.stop_preview()
