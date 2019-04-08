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

def main():
    table = Table()
    ball1 = Ball(1, (255, 0, 0), True)
    ball1.place(table.space, (200,200))

    ball2 = Ball(2, (255, 255, 0), True)
    ball2.place(table.space, (300, 220))
    while(True):
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
        table.space.debug_draw(pymunk.pygame_util.DrawOptions(table.screen))
        pygame.display.update()
        table.space.step(1.0/60.0)
        table.clock.tick(60)


main()