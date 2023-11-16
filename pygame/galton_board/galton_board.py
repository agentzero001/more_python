import pymunk.pygame_util
import pygame as pg
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

ball_mass, ball_radius = 1, 7
segment_thickness = 6

a, b, c, d = 10, 100, 18, 40
x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b
L1, L2, L3, L4 = (x1, -100), (x1, y1), (x2, y2), (x2, y3)
R1, R2, R3, R4 = (x4, -100), (x4, y1), (x3, y2), (x3, y3)
B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)


def create_ball(space, pos, mass, radius):
    ball_mass = mass
    ball_radius = radius
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = .1
    ball_shape.friction = .1
    space.add(ball_body, ball_shape)

def create_segment(begin, end, thickness, space, color): 
    segment_shape = pymunk.Segment(space.static_body, begin, end, thickness)
    segment_shape.color = pg.color.THECOLORS[color]
    space.add(segment_shape)
    
    
def create_peg():
    
    pass

platforms = (L1, L2), (L2, L3), (L3, L4), (R1, R2), (R2, R3), (R3, R4)
for platform in platforms:
    create_segment(*platform, segment_thickness, space, 'darkolivegreen')

create_segment((0,HEIGHT), (WIDTH,HEIGHT), 20, space, 'darkolivegreen')

while True:
    surface.fill(pg.Color('black'))
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                click = True
        if i.type == pg.MOUSEBUTTONUP:
                create_ball(space, i.pos, ball_mass, ball_radius)
                click = False
                a = 0       
                    
    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)
    