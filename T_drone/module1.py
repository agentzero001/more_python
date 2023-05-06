import pygame as pg

# def key_controller():
#     a=0
#     pg.init()
#     pg.display.set_mode((200, 200))
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_w:
#                     print('w pressed')
#                 elif event.key == pg.K_k:
#                     print('k pressed')
#         keys = pg.key.get_pressed()
#         if keys[pg.K_a]:
#             a+=1
#             print(a)
            
pg.init()
pg.display.set_mode((200, 200))

            
def getKey(kname):
    pressed = False
    for eve in pg.event.get(): pass
    keyInput = pg.key.get_pressed()
    myKey = getattr(pg, 'K_{}'.format(kname))
    if keyInput[myKey]:
       pressed = True
    pg.display.update()
    
    return pressed

while True:
    print(getKey('a'))



if __name__ == '__main__':
    pass
