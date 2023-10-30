import pygame as pg

pg.init()

pg.display.set_mode([200,200])

running = True

    
def check_events():
    global running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            #pg.quit()
            #sys.exit()
            running = False
        

while running:
    check_events()
    pg.display.update()