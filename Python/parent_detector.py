from gpiozero import MotionSensor
from picamera import PiCamera
import time

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	print("Motion not detected!")
	camera.stop_preview()
	time.sleep(2)
