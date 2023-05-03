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



while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print('w pressed')
            elif event.key == pg.K_k:
                print('k pressed')

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        print(pg.K_a)


# if __name__ == '__main__':
#    init()







def key_controller():
    a=0
    pg.init()
    pg.display.set_mode((200, 200)) # create a window for pygame to receive events
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    print('w pressed')
                elif event.key == pg.K_k:
                    print('k pressed')
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            a+=1
            print(a)



