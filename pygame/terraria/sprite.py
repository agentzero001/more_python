import pygame as pg
from settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self, group, image=pg.Surface([TILE_SIZE,TILE_SIZE]), pos=(0,0)):
        super().__init__(group)
        self.image = image
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)
    
    def update(self):
        self.rect.move_ip(0, 5)
        
