from typing import Any
import pygame as pg
from const import *
from utils import get_scaled_image
      
        
class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, piece_name, board):
        self.x = x
        self.y = y
        self.board = board
        pg.sprite.Sprite.__init__(self)
        self.img_res = [TILE_SIZE - 16] * 2
        self.image = get_scaled_image('assets/{}_{}.png'.format(color, piece_name), self.img_res)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.idx_pos = self.x // TILE_SIZE, self.y // TILE_SIZE
        self.assign_pos()
            
    def assign_pos(self):
        self.board.chess_matrix[self.idx_pos[1]][self.idx_pos[0]] = self

class Queen(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'queen', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
          
        
class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'king', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        
class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'pawn', board)
        
    # def update(self):
    #     pass
                
class Knight(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'knight', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
    
class Rook(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'rook', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
class Bishop(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'bishop', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        