import pygame as pg
#from pygame.sprite import Group
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.image = pg.Surface((WIDTH // 10, HEIGHT // 20))
        self.image.fill('black')
        
        self.rect = self.image.get_rect(midbottom = (WIDTH // 2, HEIGHT - 20))