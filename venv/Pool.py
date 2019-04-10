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
from Table import Table
from Ball import Ball
class Pool:

    BALL_RADIUS = 23

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

    def main(self):
        table = Table()

        ball1 = Ball(16, (255, 0, 0, 255), True)
        ball1.place(table.space, (200,200))

        # ball2 = Ball(2, (255, 255, 0), True)
        # ball2.place(table.space, (300, 220))
        collHand = table.space.add_collision_handler(10, 11)
        collHand.begin = self.callback
        while(True):
            # print(collHand.separate)
            # while(not collHand.separate == None):
            #     print(collHand.separate)
            table.display()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if table.textinput.update(events):
                if table.textStatus == "Angle":
                    table.angle = table.textinput.input_string
                    table.textinput.clear_text()
                    table.textStatus = "Power"
                    table.angleEntered = True
                else:
                    table.textStatus = "Angle"
                    table.power = table.textinput.input_string
                    table.textinput.clear_text()
                    table.powerEntered = True

                if table.angleEntered and table.powerEntered:
                    ball1.move(table.angle, table.power)
                    table.angleEntered = False
                    table.powerEntered = False
            options = pymunk.pygame_util.DrawOptions(table.screen)
            table.space.debug_draw(options)


            doFriction(ball1)
            # for item in table.space.bodies:
            # #     if(type(item) == type(ball1)):
            #     doFriction(item)
            pygame.display.update()
            table.space.step(1.0/60.0)
            table.clock.tick(60)

    def callback(self, arbiter, space, data):
        ball = arbiter.shapes[0]
        hole = arbiter.shapes[1]
        print(ball.body.mass)
        # print((list(ball.body.shapes))[0].mass)
        # print((list(ball.body.shapes))[1].mass)
        # print((list(ball.body.shapes))[2].mass)
        # print((list(ball.body.shapes))[3].mass)
        return False;

def doFriction(ball):
    velX = ball.body.velocity.x
    velY = ball.body.velocity.y
    # print(ball.body.velocity)
    if abs(velX)<5 and abs(velY)<5:
        ball.frictionCounter = ball.frictionCounter + 1
        # print("BALL COUNTER: ", ball.frictionCounter)
        if ball.frictionCounter > 30:
            velX = 0
            velY = 0
    else:
        ball.frictionCounter = 0
    ball.body.velocity = pymunk.Vec2d(velX, velY)

p = Pool()
Pool.main(p)