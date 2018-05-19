#!/usr/bin/env python

import threading
import time
import sys

import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

GAME_LAYOUT = {
    20: [0, None, 1, 0, 0],
    21: [0, None, 1, 0, 50],
    22: [0, None, 1, 0, 100],
    23: [0, None, 1, 0, 150],
    24: [0, None, 1, 0, 200],
    25: [0, None, 1, 0, 250],
    26: [0, None, 1, 0, 300],
    27: [0, None, 1, 0, 300],
}


def pin_callback(channel):
    #print('Callback channel: {}'.format(channel))
    event = GAME_LAYOUT[channel][1]
    pygame.event.post(event)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configure the pins to a point value:
count = 0
for pin in GAME_LAYOUT:
    count += 1
    GPIO.setup(pin, GPIO.IN)
    event_no = pygame.USEREVENT + count
    GAME_LAYOUT[pin][0] = event_no
    GAME_LAYOUT[pin][1] = pygame.event.Event(event_no)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=pin_callback,
                          bouncetime=1000)


# Red Button connected to BCM 13
RED_IN = 13
GPIO.setup(RED_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup the pygame events to be fired by the GPIO events
RED_USER = pygame.USEREVENT + 100
RED_EVENT = pygame.event.Event(RED_USER)


def reset_callback(channel):
    print('reset_callback')
    pygame.event.post(RED_EVENT)


GPIO.add_event_detect(RED_IN, GPIO.FALLING, callback=reset_callback,
                      bouncetime=1000)


def get_current_time():
    return int(round(time.time() * 1000))


def main():
    # Initalize the screen
    pygame.init()

    # Event loop
    ball = 1
    score = 0
    while True:
        current_time = get_current_time()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == RED_USER:
                print('Red triggered')
                score = 0
                ball = 1
            for pin in GAME_LAYOUT:
                if GAME_LAYOUT[pin][0] == event.type:
                    #print('Event: {}'.format(event.type))
                    points = GAME_LAYOUT[pin][4]
                    score += points
                    print('You earn {} points on ball {}'.format(points, ball))
                    print('SCORE: {}'.format(score))
                    ball += 1
                    break
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
