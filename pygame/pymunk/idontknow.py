import pymunk.pygame_util
import pygame as pg
from random import randrange
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 900
FPS = 60

click = False
a = 0

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000


def create_segment(space, begin, end, thickness=10): 
    segment_shape = pymunk.Segment(space.static_body, begin, end, thickness)
    segment_shape.elasticity = .5
    segment_shape.friction = .2
    space.add(segment_shape)

def create_box(space, mass, size, pos=(WIDTH // 2, HEIGHT-50)):
    box_mass, box_size = mass, size
    box_moment = pymunk.moment_for_box(box_mass, box_size)
    box_body = pymunk.Body(box_mass, box_moment)
    box_body.position = pos
    box_shape = pymunk.Poly.create_box(box_body, box_size)
    box_shape.color = (50, 50, 50, 100)
    space.add(box_body, box_shape)
    
    
create_box(space, 1, (50, 50))
create_segment(space, (0, HEIGHT), (WIDTH, HEIGHT))
create_segment(space, (0, 0), (0, HEIGHT))


while True:
    surface.fill(pg.Color('black'))
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
            
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)