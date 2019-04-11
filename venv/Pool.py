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
import csv

STATE_FILE = "state.txt"

BALL_RADIUS = 11.5

FOOT_SPOT = (625, 225)
EIGHT_BALL_POS = (FOOT_SPOT[0] + BALL_RADIUS * 2, FOOT_SPOT[1])
TRIANGLE_COORDS = [FOOT_SPOT,
                   (FOOT_SPOT[0] + BALL_RADIUS, FOOT_SPOT[1] + BALL_RADIUS / 2),
                   (FOOT_SPOT[0] + BALL_RADIUS, FOOT_SPOT[1] + -BALL_RADIUS / 2),
                   (FOOT_SPOT[0] + BALL_RADIUS * 2, FOOT_SPOT[1] + BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS * 2, FOOT_SPOT[1] + -BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS * 3, FOOT_SPOT[1] + BALL_RADIUS / 2),
                   (FOOT_SPOT[0] + BALL_RADIUS * 3, FOOT_SPOT[1] + -BALL_RADIUS / 2),
                   (FOOT_SPOT[0] + BALL_RADIUS * 3, FOOT_SPOT[1] + BALL_RADIUS * 1.5),
                   (FOOT_SPOT[0] + BALL_RADIUS * 3, FOOT_SPOT[1] + -BALL_RADIUS * 1.5),
                   (FOOT_SPOT[0] + BALL_RADIUS * 4, FOOT_SPOT[1] + 0),
                   (FOOT_SPOT[0] + BALL_RADIUS * 4, FOOT_SPOT[1] + BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS * 4, FOOT_SPOT[1] + BALL_RADIUS * 2),
                   (FOOT_SPOT[0] + BALL_RADIUS * 4, FOOT_SPOT[1] + -BALL_RADIUS),
                   (FOOT_SPOT[0] + BALL_RADIUS * 4, FOOT_SPOT[1] + -BALL_RADIUS * 2)]
BALL_INFO = [
    (1, (255, 255, 0), False),
    (2, (0, 0, 255), False),
    (3, (255, 0, 0), False),
    (4, (138, 43, 226), False),
    (5, (255, 69, 0), False),
    (6, (0, 128, 0), False),
    (7, (128, 0, 0), False),
    (8, (0, 0, 0), False),
    (9, (255, 255, 0), True),
    (10, (0, 0, 255), True),
    (11, (255, 0, 0), True),
    (12, (138, 43, 226), True),
    (13, (255, 69, 0), True),
    (14, (0, 128, 0), True),
    (15, (128, 0, 0), True),
    (16, (255, 255, 255), False)]


class Pool:
    def __init__(self):
        self.sunkBalls = []
        self.points = 0
        self.table = Table()
        self.ready = True
        self.balls = self.addBalls()
        self.writeState(STATE_FILE)
        self.anglerBody = pymunk.Body(0, math.inf, 1)
        self.angler = pymunk.Segment(self.anglerBody, (2000,2000), (2001, 2001), 1)
        self.angler.filter = pymunk.ShapeFilter(categories=2, mask=2)
        self.table.space.add(self.angler, self.anglerBody)

    def main(self):

        collHand = self.table.space.add_collision_handler(10, 11)
        collHand.begin = self.callback

        while(True):
            #check for input from a file?
            #maybe see if you can throw an event from a seaparte program

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
                    self.ready = False;
                    self.writeState(STATE_FILE)
                    self.balls[15].move(self.table.angle, self.table.power)
                    self.table.angleEntered = False
                    self.table.powerEntered = False
            for b in self.balls:
                doFriction(b) #this needs to apply to every ball
            self.ready = self.checkDone()
            if self.ready:
                self.writeState(STATE_FILE)
            self.adjustAngler()

            options = pymunk.pygame_util.DrawOptions(self.table.screen)
            self.table.space.debug_draw(options)
            pygame.display.update()
            self.table.space.step(2.0/60.0)
            self.table.clock.tick(60)

    def adjustAngler(self):
        self.anglerBody.position = self.balls[15].body.position
        self.angler.unsafe_set_endpoints(self.balls[15].body.world_to_local(self.balls[15].body.position),
                                         (self.balls[15].body.world_to_local(self.balls[15].body.position).x, 20))
        self.angler.body.angle = -math.radians(-int(self.table.angle))-math.pi/2

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
        if num == 16:
            ball.body.position = 225, 225
            self.points = self.points - 1
        else:
            self.sunkBalls.append(ball)
            index = self.sunkBalls.index(ball)
            # ball.body.body_type = 1
            self.points = self.points + 1
            ball.body.position=1025, 23+(index*23)
        ball.body.velocity = (0,0)

    def checkDone(self):
        done = True
        for s in self.table.space.bodies:
            if (not s.velocity.x == 0) or (not s.velocity.y == 0):
                done = False
        return done

    def addBalls(selfy):
        balls = []
        possible = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14]

        #most balls
        for i in range(len(possible)):
            index = random.choice(possible)
            possible.remove(index)
            ball = Ball(BALL_INFO[index][0], BALL_INFO[index][1], BALL_INFO[index][2])
            balls.append(ball)
            ball.place(selfy.table.space, TRIANGLE_COORDS[i])

        #eight ball
        ball = Ball(BALL_INFO[7][0], BALL_INFO[7][1], BALL_INFO[7][2])
        balls.append(ball)
        ball.place(selfy.table.space, EIGHT_BALL_POS)
        #cue ball
        ball = Ball(BALL_INFO[15][0], BALL_INFO[15][1], BALL_INFO[15][2])
        balls.append(ball)
        ball.place(selfy.table.space, (225, 225))

        return balls

    def writeState(self, filename):
        f = open(filename, "w+")
        if self.ready:
            f.write("READY,Y\n")
        else:
            f.write("READY,N\n")
        f.write("SCORE,"+str(self.points)+"\n")
        for b in self.balls:
            if b.striped:
                strip = 1
            else:
                strip = 0
            nl = str(b.num) + "," + str(strip) + "," + str(b.body.position.x) + "," + str(b.body.position.y) + "\n"
            f.write(nl)
        # print("writing")





def doFriction(ball): #cheap version of friction
    velX = ball.body.velocity.x
    velY = ball.body.velocity.y
    if abs(velX)<5 and abs(velY)<5:
        ball.frictionCounter = ball.frictionCounter + 1
        if ball.frictionCounter > 30:
            velX = 0
            velY = 0
    else:
        ball.frictionCounter = 0
    ball.body.velocity = pymunk.Vec2d(velX, velY)

p = Pool()
Pool.main(p)