import pygame as pg
from const import *

class Board:
    def __init__(self, app):
        self.app = app
        self.tile_size = TILE_SIZE
        self.color = BOARD_COLOR_2
        
    
                
    def draw(self):
        k = 0
        for i in range(0, WIDTH, TILE_SIZE*2):
            for j in range(0, HEIGHT, TILE_SIZE):
                self.surface = pg.Surface((TILE_SIZE, TILE_SIZE))
                self.surface.fill(BOARD_COLOR_2)
                if k % 2 == 0:
                    self.app.screen.blit(self.surface, (i, j))
                else:
                    self.app.screen.blit(self.surface, (i+TILE_SIZE, j))
                k += 1