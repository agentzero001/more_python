import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

# def getKey(kname):
#    ans = True
#    for eve in pg.event.get(): pass
#    keyInput = pg.key.get_pressed()
#    myKey = getattr(pg, 'K_{}'.format(kname))
#
#    return ans

x = 0

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print('w pressed')
            elif event.key == pg.K_k:
                print('k pressed')

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        print('a pressed')


# if __name__ == '__main__':
#    init()
