#!/usr/bin/env python

import time

import pygame
from pygame.locals import *

def get_current_time():
    return int(round(time.time() * 1000))

class Target(object):
    def __init__(self, value):
        self.value = value
        self.latched = False
        self.latch_time = 0

    def trigger(self):
        if self.latched:
            return False
        self.latched = True
        # Latch for 1 second
        self.latch_time = get_current_time() + 1000
        return True

    def clear(self):
        self.latched = False
        self.latch_time = 0

CHECK_LATCHES_INTERVAL = 100
CHECK_LATCHES = pygame.USEREVENT + 1

def main():
    # Initalize the screen
    pygame.init()
    screen = pygame.display.set_mode((150, 150))
    pygame.display.set_caption('pygame')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Setup targets
    score = 0
    target = [Target(100), Target(1000)]
    print(target)
    print(target[0])

    # Setup timers
    pygame.time.set_timer(CHECK_LATCHES, CHECK_LATCHES_INTERVAL)

    # Event loop
    while True:
        current_time = get_current_time()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    hit = target[0].trigger()
                    if hit:
                        score += target[0].value
                        print(score)
                if event.key == K_DOWN:
                    hit = target[1].trigger()
                    if hit:
                        score += target[1].value
                        print(score)
            if event.type == CHECK_LATCHES:
                for t in target:
                    if t.latch_time < current_time:
                        t.clear()

        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
