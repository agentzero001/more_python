from typing import Any
import pygame as pg
from const import *
from utils import get_scaled_image
      
        
class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, piece_name):
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)
        self.img_res = [TILE_SIZE - 16] * 2
        self.image = get_scaled_image('assets/{}_{}.png'.format(color, piece_name), self.img_res)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'queen')
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        
        
class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'king')
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        
class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'pawn')
        
    # def update(self):
    #     pass
                
class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'knight')
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
    
class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'rook')
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color, 'bishop')
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        