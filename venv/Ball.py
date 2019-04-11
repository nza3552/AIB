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
import pymunk.shapes


f = pygame.font.Font(None, 32)
class Ball:
    def __init__(self, num, col, striped):
        self.frictionCounter = 0
        self.radius = 23/2
        self.mass = 1.000000 + (num*0.00000001)
        self.num = num
        self.col = col
        self.striped = striped

        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius, (0,0))
        self.moment = math.inf
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.body_type = 0

        self.shapeID = pymunk.Circle(self.body, num, (0,0))
        self.shape3 = pymunk.Circle(self.body, 1, (0,0))

        if self.striped:
            self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
            self.shape2 = pymunk.Poly(self.body, ((-self.radius,3), (self.radius,3), (self.radius,-3), (-self.radius,-3)))
            self.shape.color = (255,255,255,255)

            self.shape2.color = (col)
            self.shape2.filter = pymunk.ShapeFilter(categories=1)
        else:
            self.shape = pymunk.Circle(self.body, self.radius, (0, 0))
            self.shape.color = (col)

        self.shape.elasticity = 1
        self.shape.friction = 0.0
        self.shape.filter = pymunk.ShapeFilter(categories=1)
        self.shape3.filter = pymunk.ShapeFilter(categories=4, mask=4)
        self.shape3.collision_type = 10

    def place(self, space, loc):
        self.body.position = loc
        if len(self.body.shapes)==4:
            space.add(self.body, self.shape, self.shape2, self.shape3)
        else:
            space.add(self.body, self.shape, self.shape3)

    def move(self, angle, power):
        angle = math.radians(float(angle))
        x = math.cos(angle)
        y = math.sin(angle)
        xPower = x*float(power)*10
        yPower = y*float(power)*10

        print("moving")
        self.body.apply_impulse_at_local_point((xPower,yPower), (0,0))
