import os, sys
import pygame
import pygame.gfxdraw
import random
import math
from pygame.locals import *

BALL_RADIUS = 23
class Ball:
    def __init__(self, num, col, striped, loc):
        self.num = num
        self.col = col
        self.striped = striped
        self.loc = loc

        self.angle = 0
        self.vel = 0

    def display(self, screen):

        if not self.striped:
            atom_img = pygame.Surface((BALL_RADIUS, BALL_RADIUS), pygame.SRCALPHA)
            pygame.gfxdraw.aacircle(atom_img, BALL_RADIUS//2, BALL_RADIUS//2, BALL_RADIUS//2, self.col)
            pygame.gfxdraw.filled_circle(atom_img, BALL_RADIUS//2, BALL_RADIUS//2, BALL_RADIUS//2, self.col)
        else:
            atom_img = pygame.Surface((BALL_RADIUS, BALL_RADIUS), pygame.SRCALPHA)
            pygame.gfxdraw.aacircle(atom_img, BALL_RADIUS // 2, BALL_RADIUS // 2, BALL_RADIUS // 2, (255, 255, 255))
            pygame.gfxdraw.filled_circle(atom_img, BALL_RADIUS // 2, BALL_RADIUS // 2, BALL_RADIUS // 2, (255, 255, 255))
            pygame.draw.rect(atom_img, self.col, (0, (BALL_RADIUS/2)-1, BALL_RADIUS*2, 4), 4)

        myfont = pygame.font.SysFont('Impact', 15)
        textsurface = myfont.render(str(self.num), False, (0, 0, 0))
        atom_img.blit(textsurface, (4, 0))
        screen.blit(atom_img, self.loc)
