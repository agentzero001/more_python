import pygame as pg

pg.init()

WIDTH, HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))



running = True
while running:
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            running = False
    
    pg.draw.line(screen, (20, 20, 20), (240, 240), (360, 360), 20)
    pg.draw.circle(screen, (20, 20, 20), (300, 300), 60, 15)
    pg.display.update()