import pygame as pg
#print(pg.__version__)

pg.init()

screen = pg.display.set_mode((500, 500))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
        
    pg.display.update()