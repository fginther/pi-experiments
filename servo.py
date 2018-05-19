#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

SERVO_PIN = 18

GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm=GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

SetAngle(90)
SetAngle(0)
pwm.stop()
GPIO.cleanup()
