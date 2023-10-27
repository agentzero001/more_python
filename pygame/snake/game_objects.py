import pygame as pg
from random import randrange

vec2 = pg.math.Vector2

class Snake:
    
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE -2, game.TILE_SIZE -2])
        self.rect.center = self.get_random_pos()
        self.direction = vec2(10,10)
        
    get_random_pos = lambda self: [randrange(self.size //2 , self.game.W_SIZE - self.size // 2, self.size)] * 2    
    
    def move(self):
        self.rect.move_ip(self.direction)
    
    def update(self):
        self.move()
    
    def draw(self):
        pass
        #pg.draw.rect(self.game.screen, (120,120,120), self.rect)
          
                
class Food:
    
    def __init__(self, game):
        pass
    
    def draw(self):
        pass
        #pg.draw.rect(self.game.screen, 'green', self.rect)
        
