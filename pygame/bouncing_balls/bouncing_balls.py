import pymunk.pygame_util
import pygame as pg
from read_coords import tuples_list
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 980
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
    ball_mass = 10 + bigger
    ball_radius = 20 + bigger
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 1.2
    ball_shape.friction = 1
    space.add(ball_body, ball_shape)

def create_segment(space, begin, end): 
    segment_shape = pymunk.Segment(space.static_body, begin, end, 10)
    segment_shape.elasticity = .5
    segment_shape.friction = .2
    space.add(segment_shape)

[create_segment(space, i, j) for i, j in tuples_list]


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
        #print(a)        
                    
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)
    