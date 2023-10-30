import pygame as pg
import module as m

pg.init()

pg.display.set_mode([200,200])

running = m.running

def check_events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #pg.quit()
            #sys.exit()
            running = False
      
      
def input(events):
    global running
    for event in events:
        if event.type == pg.QUIT:
            running = False
        else:
            print(event)



while running:
    input(pg.event.get())
    check_events()
    pg.display.update()