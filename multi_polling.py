#!/usr/bin/env python3

import time
import sys

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Red Button connected to BCM 13
RED_IN = 13
GPIO.setup(RED_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Blue Button connected to BCM 19
BLUE_IN = 19
GPIO.setup(BLUE_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Red LED connected to BCM 20
RED_OUT = 20
GPIO.setup(RED_OUT, GPIO.OUT)

# Blue LED connected to BCM 21
BLUE_OUT = 21
GPIO.setup(BLUE_OUT, GPIO.OUT)

# Setup initial conditions
event = 0
red_triggered = 0
blue_triggered = 0

# Set pin values to current
red = last_red = GPIO.input(RED_IN)
print(red)
if red == 0:
    sys.exit("ERROR: invalid state, red already triggered")
blue = last_blue = GPIO.input(BLUE_IN)
print(blue)
GPIO.output(BLUE_OUT, True)
if blue == 0:
    sys.exit("ERROR: invalid state, blue already triggered")

while event < 10:
    triggered = False
    now = time.time()
    # Hold the LED on for 1 second only
    if now > red_triggered + 1:
        GPIO.output(RED_OUT, False)
    if now > blue_triggered + 1:
        GPIO.output(BLUE_OUT, False)
    last_red = red
    last_blue = blue
    red = GPIO.input(RED_IN)
    blue = GPIO.input(BLUE_IN)
    if (last_red == 1) and (red == 0):
        GPIO.output(RED_OUT, True)
        # Record the time and turn on the LED
        red_triggered = now
        triggered = True
    if (last_blue == 1) and (blue == 0):
        GPIO.output(BLUE_OUT, True)
        # Record the time and turn on the LED
        blue_triggered = now
        triggered = True
   
    if triggered:
        # Increment the event counter whenever the sensor is triggered
        event += 1
        print(event)

GPIO.output(RED_OUT, False)
GPIO.output(BLUE_OUT, False)
GPIO.cleanup()
