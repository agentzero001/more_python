import pygame as pg

class Myobject(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


myobject = Myobject()
sprite_group = pg.sprite.Group() 
sprite_group.add(myobject)



print(dir(myobject))
    