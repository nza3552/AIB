from Ball import Ball
from Ball import BALL_RADIUS
import os, sys
import pygame
import pygame.gfxdraw
import random
import math
from pygame.locals import *
from TextInput import TextInput

textinput = TextInput()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()

while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))

    pygame.display.update()
    clock.tick(30)