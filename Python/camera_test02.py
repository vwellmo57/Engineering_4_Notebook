import time
import picamera

print("running!")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    camera.image_effect = 'colorswap'
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test2.jpg')

print("done!")
