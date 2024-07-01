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
                     
                    

class Queen(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'queen', board)
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        return [None]
    
    def show_capture(self, x, y, color):
        return [None]    
    
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
          
#checkmate and stalemate left here        
class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'king', board)
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        allowed_moves = self.calculate_moves(x, y)
        for coords in allowed_moves:
            try:
                blocking_piece = self.board.chess_matrix[coords[1]][coords[0]]
            except IndexError:
                blocking_piece = None
            if not(hasattr(blocking_piece, 'color')):
                self.board.blink_tile(*coords)
        return allowed_moves
    
    def show_capture(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        possible_moves = self.calculate_moves(x, y)
        kill_moves = [None]
        for coords in possible_moves:
            try:
                enemy_piece = self.board.chess_matrix[coords[1]][coords[0]]
            except IndexError:
                enemy_piece = None
            if hasattr(enemy_piece, 'color'):
                if enemy_piece.color == opp_color:
                    self.board.red_tile(*coords)
                    kill_moves.append(coords)    
        return kill_moves        
    
    calculate_moves = lambda self, x, y: [(dx + x, dy + y)
                                          for dx in range(-1, 2) 
                                          for dy in range(-1, 2)
                                          if not(dx == 0 and dy == 0)]
                
        
        
#only thing left to do here is pawn promotion.
class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'pawn', board)
        self.touched = False
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        allowed_move1 = x, y+1 if self.color == 'black' else y-1
        blocking_piece = self.board.chess_matrix[allowed_move1[1]][allowed_move1[0]]
        if hasattr(blocking_piece, 'color'):
            return [None]
        
        self.board.blink_tile(*allowed_move1)
        self.picked = True
        if self.touched == False:
            allowed_move2 = x, y+2 if self.color == 'black' else y-2
            blocking_piece = self.board.chess_matrix[allowed_move2[1]][allowed_move2[0]]
            if hasattr(blocking_piece, 'color'):
                return [allowed_move1, None]
            
            self.board.blink_tile(*allowed_move2)
            return allowed_move1, allowed_move2
        return [allowed_move1]
    
    def show_capture(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        move_direction = y - 1 if player == 0 else y + 1
        pos_move1 = self.board.chess_matrix[move_direction][x-1]
        try:
            pos_move2 = self.board.chess_matrix[move_direction][x+1]
        except IndexError:
            pos_move2 = None
        allowed_move1 = None
        allowed_move2 = None    
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
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        return [None]
    
    def show_capture(self, x, y, color):
        return [None]    
            
                
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
    
class Rook(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'rook', board)
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        return [None]
    
    def show_capture(self, x, y, color):
        return [None]
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
    
class Bishop(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'bishop', board)
        
    def pick(self, x, y):
        self.board.border_tile(x, y)
        return [None]
    
    def show_capture(self, x, y, color):
        return [None]
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def update(self):
        pass
        
        
