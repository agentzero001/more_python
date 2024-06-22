import pygame as pg
from const import *

class Board:
    def __init__(self, app):
        self.app = app
        self.tile_size = TILE_SIZE
        self.color = BOARD_COLOR_2
        self.chess_matrix = [[0] * 8 for i in range(8)]
        print(self.chess_matrix)
                        
    def draw(self):
        k = 0
        for i in range(0, WIDTH, TILE_SIZE*2):
            for j in range(0, HEIGHT, TILE_SIZE):
                self.surface = pg.Surface((TILE_SIZE, TILE_SIZE))
                self.surface.fill(BOARD_COLOR_2)
                if k % 2 == 0:
                    self.app.surface.blit(self.surface, (i, j))
                else:
                    self.app.surface.blit(self.surface, (i+TILE_SIZE, j))
                k += 1
       