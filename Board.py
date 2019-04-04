# import Ball
import os, sys
import pygame
import pygame.gfxdraw
from pygame.locals import *

BALL_INFO = [
    (1, (255, 255, 0), False),
    (2, (0, 0, 255), False),
    (3, (255, 0, 0), False),
    (4, (138, 43, 226), False),
    (5, (255, 69, 0), False),
    (6, (0, 128, 0), False),
    (7, (128, 0, 0), False),
    (8, (0, 0, 0), False),
    (1, (255, 255, 0), True),
    (2, (0, 0, 255), True),
    (3, (255, 0, 0), True),
    (4, (138, 43, 226), True),
    (5, (255, 69, 0), True),
    (6, (0, 128, 0), True),
    (7, (128, 0, 0), True),
    (16, (255, 255, 255), False)]

class Board:
    def buildBoard(self):
        pygame.init()
        screen=pygame.display.set_mode((880, 440))
        pygame.display.set_caption('Billards')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((10, 108, 3))

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Ball 1", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=background.get_width() / 2)
            background.blit(text, textpos)
        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock = pygame.time.Clock()

        balls = self.constructBalls()
        self.positionBalls(screen, balls)
        pygame.display.flip()

        while 1 == 1:
            clock.tick(60)

    def constructBalls(self):
        balls = []
        for info in BALL_INFO:
            balls.append(Ball.makeBall(Ball(), info[0], info[1], info[2]))
        return balls

    def positionBalls(self, screen, balls):
        screen.blit(balls[0], (0, 0))
        screen.blit(balls[1], (50, 0))
        screen.blit(balls[2], (100, 0))






class Ball:
    # num = 0
    # col = (0, 0, 0)
    # stripe = False

    def makeBall(self, num, col, stripe):
        atom_img = pygame.Surface((23, 23), pygame.SRCALPHA)
        # draw.circle is not anti-aliased and looks rather ugly.
        # pygame.draw.circle(ATOM_IMG, (0, 255, 0), (15, 15), 15)
        # gfxdraw.aacircle looks a bit better.
        pygame.gfxdraw.aacircle(atom_img, 11, 11, 11, col)
        pygame.gfxdraw.filled_circle(atom_img, 11, 11, 11, col)
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        textsurface = myfont.render("  " + str(num), False, (0, 0, 0))
        atom_img.blit(textsurface, (0, 0))
        # atom_img = pygame.Surface((50,50), pygame.SRCALPHA)
        # pygame.draw.rect(atom_img, col, (0, 0, 50, 50), 5)
        return atom_img

Board.buildBoard(Board())
