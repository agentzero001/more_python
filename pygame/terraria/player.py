import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, group, image=pg.Surface([TILE_SIZE*2,TILE_SIZE*3]), pos=(WIDTH//2,HEIGHT//2)):
        super().__init__(group)
        self.image = image
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)
        
        
    def control(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_d]:
            self.rect.x += 1
            
        if keys[pg.K_a]:
            self.rect.x -= 1
            
    def update(self):
        self.control()