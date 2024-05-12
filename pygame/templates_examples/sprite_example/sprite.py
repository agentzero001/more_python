import pygame as pg
from settings import *

class Object(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pg.Surface((50, 80))
        self.rect = self.image.get_rect(topleft=(WIDTH // 2, HEIGHT //2))
        self.image.fill('black')
        
   
class Square(pg.sprite.Sprite):
    def __init__(self, col, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
                
        
    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.kill()
        