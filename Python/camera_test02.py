import time
import picamera

print("running! 1")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'colorswap'   
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test2.jpg')

print("done! 1")

print("running 2!")

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.image_effect = 'pastel'
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('test3.jpg')

print("done! 2")
