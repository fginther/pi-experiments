#!/usr/bin/env python

import threading
import time
import sys

import RPi.GPIO as GPIO
import pygame
from pygame.locals import *


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Red Button connected to BCM 13
RED_IN = 13
GPIO.setup(RED_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Blue Button connected to BCM 19
BLUE_IN = 19
GPIO.setup(BLUE_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup the pygame events to be fired by the GPIO events
BLUE_USER = pygame.USEREVENT + 1
RED_USER = pygame.USEREVENT + 2
BLUE_EVENT = pygame.event.Event(BLUE_USER)
RED_EVENT = pygame.event.Event(RED_USER)


def blue_callback(channel):
    #print('blue_callback')
    pygame.event.post(BLUE_EVENT)


def red_callback(channel):
    #print('red_callback')
    pygame.event.post(RED_EVENT)


GPIO.add_event_detect(BLUE_IN, GPIO.FALLING, callback=blue_callback,
                      bouncetime=1000)
GPIO.add_event_detect(RED_IN, GPIO.FALLING, callback=red_callback,
                      bouncetime=1000)


def get_current_time():
    return int(round(time.time() * 1000))


def main():
    # Initalize the screen
    pygame.init()

    # Event loop
    while True:
        current_time = get_current_time()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == BLUE_USER:
                print('Blue triggered')
            if event.type == RED_USER:
                print('Red triggered')
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
