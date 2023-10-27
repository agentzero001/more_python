import pygame as pg
from random import randrange

vec2 = pg.math.Vector2

class Snake:
    
    def __init__(self, game):
        
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE -2, game.TILE_SIZE -2])
        
    def update(self):
        pass
    
    
    def draw(self):
        pg.draw.rect(self.game.screen, 'green', self.rect)
        
        
        
        
        
        
        
        
class Food:
    
    def __init__(self, game):
        pass
    
    
    def draw(self):
        pass
        #pg.draw.rect(self.game.screen, 'green', self.rect)
        
