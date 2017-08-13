#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

for i in range (10):
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)
	time.sleep(1)

