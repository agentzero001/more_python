import sys 
import numpy as np
import pygame as pg
 
pg.init()

RES = WIDTH, HEIGHT = 800, 800
SCALE_FACTOR = 1
SIZE = 200
FPS = 60
GREY = (100,100,100)
POINTS = [(-10, -10), (100, 100), (200, 200), (400, 200)]

def draw_curve(f, a, b, n=200):
    t = np.linspace(a, b, n)
    c_x, c_y = f(t)
    pg.draw.aalines(screen, GREY, False, [conv_coords(x, y) for x,y in zip(c_x, c_y)]  , 1) 



k = 0

font = pg.font.Font(None, 24)
fpsClock = pg.time.Clock()
screen = pg.display.set_mode(RES)

conv_coords = lambda x, y: ((x + WIDTH // 2), (-y  + HEIGHT // 2))
draw_point = lambda x, y, color=GREY, radius=2: pg.draw.circle(screen, color, conv_coords(x,y), radius)

a = lambda t: (100*np.sin(2*t), 100*np.cos(3*t))

print(conv_coords(20, 20))


while True:
    k %=1    
    screen.fill((20, 20, 20))
    pg.draw.line(screen, (100,100,100), conv_coords(-SIZE, 0), conv_coords(SIZE, 0), 1)
    pg.draw.line(screen, (100,100,100), conv_coords(0, -SIZE), conv_coords(0, SIZE), 1)    
    draw_curve(a, k*2*np.pi-.5, 2*np.pi*k)
    draw_point(100,20)
    k+=.002
    m_x, m_y  = pg.mouse.get_pos() 
    m_x, m_y = m_x - WIDTH // 2, -(m_y - HEIGHT // 2 )
    text_surface = font.render("Mouse Position: ({}, {})".format(m_x, m_y), True, GREY)
    
    #pg.draw.rect(screen, 'White', (*conv_coords(100,100), 100, 100), 2)
    
  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.blit(text_surface, (10, 10))
    pg.display.flip()
    
    fpsClock.tick(FPS)