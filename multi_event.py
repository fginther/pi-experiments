#!/usr/bin/env python3

import threading
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
triggered = False

def common_trigger(channel):
    global event
    global triggered
    triggered = True
    event += 1

def blue_clear():
    GPIO.output(BLUE_OUT, False)

def red_clear():
    GPIO.output(RED_OUT, False)

def blue_callback(channel):
    common_trigger(channel)
    GPIO.output(BLUE_OUT, True)
    threading.Timer(1, blue_clear).start()

def red_callback(channel):
    common_trigger(channel)
    GPIO.output(RED_OUT, True)
    threading.Timer(1, red_clear).start()

GPIO.add_event_detect(BLUE_IN, GPIO.FALLING, callback=blue_callback,
                      bouncetime=1000)
GPIO.add_event_detect(RED_IN, GPIO.FALLING, callback=red_callback,
                      bouncetime=1000)
while True:
    if triggered:
        print(event)
        triggered = False
