import sys 
import pygame as pg
 
pg.init()
 
FPS = 60
fpsClock = pg.time.Clock()
 
RES = WIDTH, HEIGHT = 640, 480
screen = pg.display.set_mode(RES)
 

while True:
  screen.fill((0, 0, 0))
  
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  pg.display.flip()
  value = fpsClock.tick(FPS)
  print(value)