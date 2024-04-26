import pygame as pg
from pygame.sprite import _Group
from settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)