from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(11, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)



app = Flask(name)

@app.route("/", methods=["GET","POST"])
def index():
    print(request.method)
        if request.method == 'POST':
            if request.form.get('button1') == 'button1':
                SetAngle(0)
                sleep(1) 
                SetAngle(90)
                sleep(1) 
                SetAngle(0) 

pwm.stop()
GPIO.cleanup()
