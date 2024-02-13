import sys 
import numpy as np
import pygame as pg
 
pg.init()

RES = WIDTH, HEIGHT = 1600, 900


SIZE = 200
FPS = 60

screen = pg.display.set_mode(RES)
fpsClock = pg.time.Clock()

_ = False

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

world_map = {}

for j, row in enumerate(mini_map):
    for i, v in enumerate(row):
        if v:
            world_map[(i, j)] = v

[pg.draw.rect(screen, (20, 20, 20), (p[0]*50+WIDTH//4, p[1]*50+HEIGHT //4, 50, 50), 2) for p in world_map]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    pg.display.flip()
    fpsClock.tick(FPS)
        