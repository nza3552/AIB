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
from Ball import Ball

class Pocket:
    def __init__(self, space, loc, rot):
        self.radius = 40
        self.mass = 1000
        self.loc = (0,0)
        self.moment = pymunk.moment_for_poly(self.mass, ((0,0), (50,0), (50,50), (0,50)))
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.body_type = 2

        self.body.position = loc
        self.body.angle = rot
        self.shape = pymunk.Poly(self.body, ((0,0), (50,0), (50,50), (0,50)))
        self.shape.color = (10, 10, 10, 255)
        self.shape.collision_type = 11
        self.shape.filter = pymunk.ShapeFilter(categories=4, mask=4)
        space.add(self.body, self.shape)
