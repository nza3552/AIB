import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

#def add_ball(space):

def main():

    pygame.init()
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()

    space.gravity = (0.0, 0.0)

    balls = []
    screen = pygame.display.set_mode((1000, 400))
    draw_options = pymunk.pygame_util.DrawOptions(screen)


    ticks_to_next_ball = 10
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        space.step(1/50.0)
        screen.fill((10, 108, 3))
        space.debug_draw(draw_options)

        pygame.display.flip()
        clock.tick(50)

def add_ball(space):
    mass = 1
    radius = 14
    moment = pymunk.moment_for_circle(mass, 0, radius) # 1
    body = pymunk.Body(mass, moment) # 2
    x = random.randint(120, 380)
    body.position = x, 200 # 3
    shape = pymunk.Circle(body, radius) # 4
    space.add(body, shape) # 5
    return shape

if __name__ == '__main__':
    sys.exit(main())