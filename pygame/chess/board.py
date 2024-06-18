import pygame as pg
from const import TILE_SIZE
from const import WIN_SIZE

class Board:
    def __init__(self, app):
        self.app = app
        self.tile_size = TILE_SIZE
        self.surface = pg.surface.Surface(WIN_SIZE)
        self.surface.fill((100, 100, 100))
        self.rect = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE)
        pg.draw.rect(self.surface,(100, 0, 0), self.rect)
                
    def draw(self):
        self.app.screen.blit(self.surface, (0, 0))