#!/usr/bin/env python3

import time
import sys

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

MIN = 20
MAX = 28
# Proximity vIN connected to BCM 26
for in_pin in range(MIN, MAX):
    print('Setting input pin: {}'.format(in_pin))
    GPIO.setup(in_pin, GPIO.IN)

# LED connected to BCM 17
GPIO.setup(17, GPIO.OUT)

# Setup initial conditions
pin_triggered = 0

while True:
    now = time.time()
    for in_pin in range(MIN, MAX):
        if not GPIO.input(in_pin):
            print('Triggered: {}'.format(in_pin))

GPIO.output(17, False)
