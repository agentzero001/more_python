import pymunk.pygame_util
import pygame as pg
from random import randrange
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1600, 1000
FPS = 60

click = False
a = 0

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000

def create_ball(space, pos, bigger=0):
    ball_mass = 10 + bigger * 8
    ball_radius = 20 + bigger
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 1.2
    ball_shape.friction = 1
    ball_shape.color = (94, 59, 12, 10)
    space.add(ball_body, ball_shape)

def create_segment(space, begin, end, thickness=20): 
    segment_shape = pymunk.Segment(space.static_body, begin, end, thickness)
    segment_shape.elasticity = .5
    segment_shape.friction = .2
    space.add(segment_shape)
    
box_mass, box_size = 1, (40, 20)
for x in range(120, WIDTH - 60, box_size[0]):
    for y in range(HEIGHT // 2, HEIGHT - 20, box_size[1]):
        box_moment = pymunk.moment_for_box(box_mass, box_size)
        box_body = pymunk.Body(box_mass, box_moment)
        box_body.position = x, y
        box_shape = pymunk.Poly.create_box(box_body, box_size)
        box_shape.elasticity = .1
        box_shape.friction = .4
        box_shape.color = [randrange(180) for i in range(3)] + [100]
        print([randrange(256) for i in range(4)])
        space.add(box_body, box_shape)

#create_segment(space, (WIDTH,HEIGHT), (WIDTH,0))
create_segment(space, (0,HEIGHT), (WIDTH,HEIGHT))
create_segment(space, (0,HEIGHT), (0, 0))
create_segment(space, (0,0), (WIDTH, 0))


while True:
    surface.fill(pg.Color('black'))
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                click = True
        if i.type == pg.MOUSEBUTTONUP:
                create_ball(space, i.pos, bigger=a)
                click = False
                a = 0
    if click:
        a += 2
                    
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)
    