import pygame as pg


def init():
    pg.init()
    win = pg.display.set_mode((400,400))

def getKey(kname):
    ans = True
    for event in pg.event.get(): pass
    keyInput = pg.key.get_pressed()
    myKey = getattr(pg, 'K_{}'.format(kname))



if __name__ == '__main__':
    init()


