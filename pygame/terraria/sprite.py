import pygame as pg
from pygame.sprite import _Group
from settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self, group, image=pg.Surface([TILE_SIZE, TILE_SIZE]), pos=(0, 0)):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        