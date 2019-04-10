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

class Border:
    def __init__(self, space, a, rotate):

        a = a;
        b = (a[0]+25, a[1]-25)
        c = (a[0]+25, a[1]-355)
        d = (a[0], a[1]-380)

        self.mom = pymunk.moment_for_poly(1000, (a, b, c, d))
        self.bod = pymunk.Body(1000, self.mom)
        self.bod.body_type = 2
        self.shape = pymunk.Poly(self.bod, (a, b, c, d))
        self.bod.angle = rotate/2*math.pi
        self.shape.elasticity = 1
        self.shape.friction = 0.0

        space.add(self.bod,self.shape)
