# from Ball import Ball
# from Ball import BALL_RADIUS
import os, sys
import pygame
import pygame.gfxdraw
from pygame import font
import random
import math
from pygame.locals import *
from TextInput import TextInput
import pymunk
import pymunk.pygame_util

f = pygame.font.Font(None, 32)

class Table:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 400))
        self.screen.fill((255, 255, 255))
        self.space = pymunk.Space()
        self.clock = pygame.time.Clock()

        self.bs = new thing



        self.textStatus = "Angle"
        self.angle = 0
        self.power = 0
        self.angleEntered = False;
        self.powerEntered = False;
        self.label = pygame.font.Font(None, 32)
        self.textinput = TextInput()
    def display(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (10, 108, 3), ((0, 0),(800, 400)), 0)
        self.screen.blit(self.textinput.get_surface(), (875, 0))
        s = f.render(self.textStatus, True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(s, (800,0))
