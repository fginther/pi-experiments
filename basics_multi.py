#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

RED_LED = 20
BLUE_LED = 21
RED_BUTTON = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    if GPIO.input(RED_BUTTON):
        GPIO.output(RED_LED, True)
    else:
        GPIO.output(RED_LED, False)

for i in range (3):
    GPIO.output(RED_LED, True)
    GPIO.output(BLUE_LED, False)
    time.sleep(1)
    GPIO.output(RED_LED, False)
    GPIO.output(BLUE_LED, True)
    time.sleep(1)

GPIO.output(RED_LED, False)
GPIO.output(BLUE_LED, False)

