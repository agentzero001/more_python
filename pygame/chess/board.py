import pygame as pg
from const import *

class Board:
    def __init__(self, app):
        self.app = app
        self.tile_size = TILE_SIZE
        self.color = BOARD_COLOR_2
        self.chess_matrix = [[0] * 8 for i in range(8)]
        self.surface = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.light_surface = pg.Surface((TILE_SIZE, TILE_SIZE), pg.SRCALPHA)        
                         
    def draw(self):
        k = 0
        for i in range(0, WIDTH, TILE_SIZE*2):
            for j in range(0, HEIGHT, TILE_SIZE):
                self.surface.fill(BOARD_COLOR_2)
                if k % 2 == 0:
                    self.app.surface.blit(self.surface, (i, j))
                else:
                    self.app.surface.blit(self.surface, (i + TILE_SIZE, j))
                k += 1
                
        
    def blink_tile(self, x, y):
        self.light_surface.fill((255, 255, 255, 70))
        self.app.surface.blit(self.light_surface, (x * TILE_SIZE, y * TILE_SIZE))
        
    def red_tile(self, x, y):
        self.light_surface.fill((255, 0, 0, 100))
        self.app.surface.blit(self.light_surface, (x * TILE_SIZE, y * TILE_SIZE))
        
    def border_tile(self, x, y):
        pg.draw.rect(self.app.surface,
                     (0, 100, 30),
                     (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                     8)
        
    def red_border(self, x, y):
        pg.draw.rect(self.app.surface,
                     (127, 100, 100),
                     (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                     8)
            
    
    def black_tile(self, x, y):
        self.light_surface.fill((120, 0, 0, 100))
        self.app.surface.blit(self.light_surface, (x * TILE_SIZE, y * TILE_SIZE))  
        
    def blink_moves(self, coords, opp_color):
        for x_y in coords:
            if x_y != None:
                x, y = x_y
                field = self.chess_matrix[y][x]
                if field == 0:
                    self.blink_tile(x, y)
                else:
                    if field.color == opp_color:
                        self.red_tile(x, y)
                
        
       