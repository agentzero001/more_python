import pygame as pg

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
            
            
def getKey(kname):
   ans = True
   for eve in pg.event.get(): pass
   keyInput = pg.key.get_pressed()
   myKey = getattr(pg, 'K_{}'.format(kname))

   return ans




if __name__ == '__main__':
    pass
