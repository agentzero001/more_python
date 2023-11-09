import pymunk.pygame_util
import pygame as pg
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000


while True:
    surface.fill(pg.Color('black'))
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    pg.display.flip()
    clock.tick(FPS)
    