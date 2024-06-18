import pygame as pg
from const import *
from utils import get_scaled_image
   
class Piece(pg.sprite.Sprite):
    def __init__(self, app, x, y, color, type_):
        self.app = app
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)
        self.img_res = [TILE_SIZE - 16] * 2
        self.default_image = get_scaled_image('assets/{}_{}.png'.format(color, type_), self.img_res)
        self.image = self.default_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self):
       pass
   