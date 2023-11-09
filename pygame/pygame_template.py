import sys 
import pygame as pg
#from pg.locals import *
 
pg.init()
 
fps = 60
fpsClock = pg.time.Clock()
 
res = width, height = 640, 480
screen = pg.display.set_mode(res)
 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  pg.display.flip()
  fpsClock.tick(fps)