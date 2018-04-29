#!/usr/bin/env python3

import time
import sys

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Proximity vIN connected to BCM 26
INPUT = 26
#GPIO.setup(INPUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT, GPIO.IN)

# LED connected to BCM 17
GPIO.setup(17, GPIO.OUT)

# Setup initial conditions
event = 0
print(event)
pin_triggered = 0

# Set pin values to current
pin = last_pin = GPIO.input(INPUT)
if pin == 0:
    sys.exit("ERROR: invalid state, pin already triggered")

while event < 10:
    now = time.time()
    if now > pin_triggered + 1:
        # Hold the LED on for 1 second only
        GPIO.output(17, False)
    last_pin = pin
    pin = GPIO.input(INPUT)
    if (last_pin == 1) and (pin == 0):
        # Increment the event counter whenever the sensor is triggered
        event += 1
        print(event)
        # Record the time and turn on the LED
        pin_triggered = time.time()
        GPIO.output(17, True)

GPIO.output(17, False)
