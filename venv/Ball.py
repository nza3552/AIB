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


class Ball:
    def __init__(self, num, col, striped):
        self.radius = 23
        self.mass = 5
        self.num = num
        self.col = col
        self.striped = striped
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius, (0,0))
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
        self.shape.friction = 50

    def place(self, space, loc):
        self.body.position = loc
        space.add(self.body, self.shape)
    def move(self, angle, power):
        angle = math.radians(float(angle))
        x = math.cos(angle)
        y = math.sin(angle)
        xPower = x*float(power)
        yPower = y*float(power)

        print("moving")
        self.body.apply_impulse_at_local_point((xPower,yPower), (0,0))
