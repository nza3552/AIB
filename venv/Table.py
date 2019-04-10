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
from Border import Border
from Pocket import Pocket

f = pygame.font.Font(None, 32)

class Table:
    def __init__(self):
        self.screen = pygame.display.set_mode((1050, 450))
        self.screen.fill((255, 255, 255))
        self.space = pymunk.Space()
        self.clock = pygame.time.Clock()

        # self.moment = pymunk.moment_for_box(1000000, (800,400))
        # self.body = pymunk.Body(1000000, self.moment)
        # self.shape = pymunk.Poly(self.body, ((0,0), (800,0),(800,400), (0,400)))
        # # self.shape.friction = 0
        # self.body.position = (0,0)
        # self.space.add(self.body, self.shape)
        self.space.damping = 0.8
        self.textStatus = "Angle"
        self.angle = 0
        self.power = 0
        self.angleEntered = False;
        self.powerEntered = False;
        self.label = pygame.font.Font(None, 32)
        self.textinput = TextInput()

        p1 = Pocket(self.space, (24, -12), math.pi/4)
        p2 = Pocket(self.space, (24, -12+402), math.pi/4)
        p3 = Pocket(self.space, (24+802, -12), math.pi/4)
        p4 = Pocket(self.space, (24+802, -12+402), math.pi/4)
        p5 = Pocket(self.space, (400, -25), 0)
        p6 = Pocket(self.space, (400, 425), 0)

        b1 = Border(self.space, (0, 415), 0)
        b2 = Border(self.space, (0, -35), 1)
        b3 = Border(self.space, (0, -35-380-20), 1)
        b4 = Border(self.space, (-850, -35), 2)
        b5 = Border(self.space, (-450-1, 415), 3)
        b6 = Border(self.space, (-450-1, 415+380+20), 3)

    def display(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (10, 108, 3), ((25, 25),(800, 401)), 0)
        self.screen.blit(self.textinput.get_surface(), (925, 0))
        s = f.render(self.textStatus, True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(s, (850,0))

    # def addBorders(self):