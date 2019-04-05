#http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/
from Ball import Ball
from Ball import BALL_RADIUS
import os, sys
import pygame
import pygame.gfxdraw
import random
import math
import pymunk
from pygame.locals import *
from TextInput import TextInput



FOOT_SPOT = (600, 200)
EIGHT_BALL_POS = (FOOT_SPOT[0] + BALL_RADIUS*2, FOOT_SPOT[1])
TRIANGLE_COORDS = [FOOT_SPOT,
                   (FOOT_SPOT[0] + BALL_RADIUS, FOOT_SPOT[1] + BALL_RADIUS/2),
                   (FOOT_SPOT[0] + BALL_RADIUS, FOOT_SPOT[1] + -BALL_RADIUS/2),
                   (FOOT_SPOT[0] + BALL_RADIUS*2, FOOT_SPOT[1] + BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS*2, FOOT_SPOT[1] + -BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS*3, FOOT_SPOT[1] + BALL_RADIUS/2),
                   (FOOT_SPOT[0] + BALL_RADIUS*3, FOOT_SPOT[1] + -BALL_RADIUS/2),
                   (FOOT_SPOT[0] + BALL_RADIUS*3, FOOT_SPOT[1] + BALL_RADIUS*1.5),
                   (FOOT_SPOT[0] + BALL_RADIUS*3, FOOT_SPOT[1] + -BALL_RADIUS*1.5),
                   (FOOT_SPOT[0] + BALL_RADIUS*4, FOOT_SPOT[1] + 0),
                   (FOOT_SPOT[0] + BALL_RADIUS*4, FOOT_SPOT[1] + BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS*4, FOOT_SPOT[1] + BALL_RADIUS*2),
                   (FOOT_SPOT[0] + BALL_RADIUS*4, FOOT_SPOT[1] + -BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS*4, FOOT_SPOT[1] + -BALL_RADIUS*2)]
BALL_INFO = [
    (1, (255, 255, 0), False),
    (2, (0, 0, 255), False),
    (3, (255, 0, 0), False),
    (4, (138, 43, 226), False),
    (5, (255, 69, 0), False),
    (6, (0, 128, 0), False),
    (7, (128, 0, 0), False),
    (9, (255, 255, 0), True),
    (8, (0, 0, 0), False),
    (10, (0, 0, 255), True),
    (11, (255, 0, 0), True),
    (12, (138, 43, 226), True),
    (13, (255, 69, 0), True),
    (14, (0, 128, 0), True),
    (15, (128, 0, 0), True),
    (16, (255, 255, 255), False)]


class Board:
    def buildBoard(self):
        pygame.init()
        screen=pygame.display.set_mode((1000, 400))
        pygame.display.set_caption('Billards')

        background = pygame.Surface((800, 400))
        background = background.convert()
        background.fill((10, 108, 3))

        backgroundDuo = pygame.Surface((200, 400))
        backgroundDuo = backgroundDuo.convert()
        backgroundDuo.fill((255, 255, 255))

        screen.blit(background, (0, 0))
        screen.blit(backgroundDuo, (800, 0))
        #drawing foot spot dot

        footSpotDotOuter = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(footSpotDotOuter, 6, 6, 6, (255, 255, 255))
        pygame.gfxdraw.filled_circle(footSpotDotOuter, 6, 6, 6, (255, 255, 255))
        footSpotDotInner = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(footSpotDotInner, 4, 4, 4, (0, 0, 0))
        pygame.gfxdraw.filled_circle(footSpotDotInner, 4, 4, 4, (0, 0, 0))
        footSpotDotOuter.blit(footSpotDotInner, (2, 2))
        screen.blit(footSpotDotOuter, FOOT_SPOT)

        balls = self.constructBalls()
        self.positionBalls(balls)
        self.initDisplay(screen, balls)

        t = TextInput()
        t.set_text_color((0, 0, 255))
        pygame.draw.rect(backgroundDuo, (255, 255, 255), (0,0, 200, 200), 5)
        # backgroundDuo.blit(t.get_surface(), (0, 0))


        pygame.display.flip()

        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if t.update(events):
                print(t.get_text())
            screen.blit(t.get_surface(), (800, 0))
            pygame.display.update()
            clock.tick(60)

    def constructBalls(self):
        balls = []
        for info in BALL_INFO:
            ball = Ball(info[0], info[1], info[2], (0,0))
            balls.append(ball)
        return balls

    def positionBalls(self, balls):
        possible = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for i in range(16):
            if balls[i].num == 8:
                balls[i].loc = EIGHT_BALL_POS
            elif balls[i].num == 16:
                balls[i].loc = (200, 200)
            else:
                ind = possible[random.randint(0, len(possible)-1)]
                balls[i].loc = TRIANGLE_COORDS[ind]
                possible.remove(ind)
        return balls
    def initDisplay(self, screen, balls):
        for ball in balls:
            print("putting ball ", ball.num, " in loc " , ball.loc)
            ball.display(screen)



def nextInt(max):
    numbers = range(1, 7) + range(9, 15)
    nu = random.choice(numbers)
    return nu

Board.buildBoard(Board())
