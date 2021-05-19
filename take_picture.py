from io import BytesIO
from picamera import PiCamera
from time import sleep


# takes a picture
def take_picture():
    my_stream = BytesIO()
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # warm up camera
    sleep(1)
    camera.capture(my_stream, 'jpeg')
    # camera.capture("/home/pi/Desktop/image.jpeg")
    camera.stop_preview()
    # read stream to a byte array
    databytes = my_stream.read()
    return databytes
