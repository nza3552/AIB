from Ball import Ball
from Ball import BALL_RADIUS
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



def main():
    textinput = TextInput()

    screen = pygame.display.set_mode((1000, 400))
    clock = pygame.time.Clock()
    textStatus = "Angle"
    angle = 0
    power = 0
    angleEntered = False;
    powerEntered = False;

    f = pygame.font.Font(None, 32)

    # b1 = Ball(1, (255, 0, 0), True, (200, 200))

    space = pymunk.Space()
    space.gravity = (0, 0)

    mass = 10
    ballInertia = pymunk.moment_for_circle(mass, 0, BALL_RADIUS, (0,0))
    ballBody = pymunk.Body(mass, ballInertia)
    ballBody.position = (200, 200)
    ballShape = pymunk.Circle(ballBody, BALL_RADIUS, (0, 0))
    ballShape.elasticity = 0.95
    ballShape.friction = 0.9
    space.add(ballBody, ballShape)


    while True:
        screen.fill((225, 225, 225))

        pygame.draw.rect(screen, (10, 108, 3), ((0, 0),(800, 400)), 0)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if textinput.update(events):
            if textStatus == "Angle":
                angle = textinput.input_string
                textinput.clear_text()
                textStatus = "Power"
                angleEntered = True
            else:
                textStatus = "Angle"
                power = textinput.input_string
                textinput.clear_text()
                powerEntered = True
        if angleEntered and powerEntered:
            print("MOVE THE BALL")
            #actually apply the force here

        screen.blit(textinput.get_surface(), (875, 0))

        s = f.render(textStatus, True, (0, 0, 0), (255, 255, 255))
        screen.blit(s, (800,0))
        space.debug_draw(pymunk.pygame_util.DrawOptions(screen))

        # b1.display(screen)


        pygame.display.update()
        clock.tick(30)


main()