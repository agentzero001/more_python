from typing import Any
import pygame as pg
from const import *
from utils import get_scaled_image
      
        
class Piece(pg.sprite.Sprite):
    def __init__(self, x, y, color, piece_name, board):
        self.x = x
        self.y = y
        self.board = board
        self.piece_name = piece_name
        self.color = color
        pg.sprite.Sprite.__init__(self)
        self.img_res = [TILE_SIZE - 16] * 2
        self.image = get_scaled_image('assets/{}_{}.png'.format(color, piece_name), self.img_res)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.idx_pos = self.rect.center[0] // TILE_SIZE, self.rect.center[1] // TILE_SIZE
        self.assign_pos(self.idx_pos[1], self.idx_pos[0])
        self.picked = False
        print(self.idx_pos)
        print(piece_name)
           
    def assign_pos(self, x, y):
        self.board.chess_matrix[x][y] = self
            
    def pick(self, pos_idx):
        if self.picked == False:        
            self.board.blink_tile(*self.idx_pos)
            print(self)
            for i in range(8):
                for j in range(8):
                    if self.board.chess_matrix[i][j] == 0:
                        self.board.blink_tile(j, i)
                    
                    elif self.board.chess_matrix[i][j].color == 'white':
                        self.board.red_tile(j, i)
            self.picked = True
        else:
            pass            
                    

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
        self.touched = False
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        allowed_move1 = x, y+1 if self.color == 'black' else y-1
        allowed_move2 = None
        self.board.blink_tile(*allowed_move1)
        if self.touched == False:
            allowed_move2 = x, y+2 if self.color == 'black' else y-2
            self.board.blink_tile(*allowed_move2)
        self.picked = True
        return allowed_move1, allowed_move2
        
    
    
    def show_capture(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        move_direction = y - 1 if player == 0 else y + 1
        allowed_move1 = None
        allowed_move2 = None
        pos_move1 = self.board.chess_matrix[move_direction][x-1]
        try:
            pos_move2 = self.board.chess_matrix[move_direction][x+1]
        except IndexError:
            pos_move2 = None
        if hasattr(pos_move1, 'color'):
            if pos_move1.color == opp_color:
                allowed_move1 = x - 1, y - 1 if player == 0 else y + 1
                self.board.red_tile(*allowed_move1)
        if hasattr(pos_move2, 'color'):
            if pos_move2.color == opp_color:
                allowed_move2 = x + 1, y - 1 if player == 0 else y + 1
                self.board.red_tile(*allowed_move2)
        return allowed_move1, allowed_move2
                        
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
        
        
