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
        self.sunkBalls = []
        self.points = 0
        self.table = Table()
        self.ready = True

        ball1 = Ball(16, (255, 0, 0, 255), True)
        ball1.place(self.table.space, (200,200))

        collHand = self.table.space.add_collision_handler(10, 11)
        collHand.begin = self.callback
        while(True):
            self.table.display()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
            if self.table.textinput.update(events):
                if self.table.textStatus == "Angle":
                    self.table.angle = self.table.textinput.input_string
                    self.table.textinput.clear_text()
                    self.table.textStatus = "Power"
                    self.table.angleEntered = True
                else:
                    self.table.textStatus = "Angle"
                    self.table.power = self.table.textinput.input_string
                    self.table.textinput.clear_text()
                    self.table.powerEntered = True

                if self.table.angleEntered and self.table.powerEntered:
                    ball1.move(self.table.angle, self.table.power)
                    self.table.angleEntered = False
                    self.table.powerEntered = False

            doFriction(ball1) #this needs to apply to every ball

            #here is where you write the state of the game to a csv file? lol

            self.ready = self.checkDone()


            options = pymunk.pygame_util.DrawOptions(self.table.screen)
            self.table.space.debug_draw(options)
            pygame.display.update()
            self.table.space.step(2.0/60.0)
            self.table.clock.tick(60)

    def callback(self, arbiter, space, data):
        ball = arbiter.shapes[0]
        hole = arbiter.shapes[1]
        self.sunk(ball)
        return False;

    def sunk(self, ball):
        t = pymunk.Space()
        striped = False
        if len(ball.body.shapes) == 4:
            striped=True
        num = math.ceil((ball.body.mass-1)*100000000)
        self.points = self.points + 1
        self.sunkBalls.append(ball)
        index = self.sunkBalls.index(ball)
        b = pymunk.Body()
        # ball.body.body_type = 1
        if num == 16:
            ball.body.position = 225, 225
        else:
            ball.body.position=1025, 23+(index*23)
        ball.body.velocity = (0,0)
        print("Points", self.points)
    def checkDone(self):
        done = True
        for s in self.table.space.bodies:
            if (not s.velocity().x == 0) or (not s.velocity().y == 0):
                done = False
        return done




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