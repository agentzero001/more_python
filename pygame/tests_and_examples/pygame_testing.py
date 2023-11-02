import pygame as pg
import module as m
import sys, os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

pg.init()

pg.display.set_mode([500,500])

running = m.running


      
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()     
     
     
      
def input(events):
    global running
    for event in events:
        if event.type == pg.QUIT:
            running = False
        else:
            print(event)





while running:
    input(pg.event.get())
    #check_events()
    pg.display.update()