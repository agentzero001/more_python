import sys 
import pygame as pg
 
pg.init()


RES = WIDTH, HEIGHT = 800, 800
SCALE_FACTOR = 1
SIZE = 200
K = 0
FPS = 60


fpsClock = pg.time.Clock()
screen = pg.display.set_mode(RES)

conv_coords = lambda x, y: ((x * SCALE_FACTOR + WIDTH // 2), (-y * SCALE_FACTOR + HEIGHT // 2))

draw_point = lambda x, y, color=(100, 100, 100), radius=2: pg.draw.circle(screen, color, conv_coords(x,y), radius)


print(conv_coords(30, 30))

while True:
    screen.fill((20, 20, 20))
    pg.draw.line(screen, (100,100,100), conv_coords(-SIZE, 0), conv_coords(SIZE, 0), 1)
    pg.draw.line(screen, (100,100,100), conv_coords(0, -SIZE), conv_coords(0, SIZE), 1)
    draw_point(10,10)
  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()
    fpsClock.tick(FPS)