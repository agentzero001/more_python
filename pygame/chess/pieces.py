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
        self.current_player = 1 if color == 'black' else 0
        pg.sprite.Sprite.__init__(self)
        self.img_res = [TILE_SIZE - 16] * 2
        self.image = get_scaled_image('assets/{}_{}.png'.format(color, piece_name), self.img_res)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.idx_x = self.x // TILE_SIZE
        self.idx_y = self.y // TILE_SIZE
        self.assign_pos(self.idx_y, self.idx_x)
        self.picked = False
        
    def pick(self):
        self.board.border_tile(self.idx_x, self.idx_y)
        possible_moves = self.calculate_moves()       
        return possible_moves
           
    def assign_pos(self, x, y):
        self.board.chess_matrix[x][y] = self         
                    
    def check_fields(self, field):
        field_obj = self.board.chess_matrix[field[1]][field[0]]
        if isinstance(field_obj, Piece):
            if field_obj.color != self.color:
                self.active = False 
                return field
            else:             
                self.active = False 
                return None
        return field
    
    #this is used for check
    def calculate_next_move(self):
        if type(self).__name__ == 'Pawn':
            moves = self.show_capturing_moves()
        else:
            moves = self.calculate_moves()
        return moves
    
    def update_idx(self):
        self.idx_x, self.idx_y = self.rect.center[0] // TILE_SIZE, self.rect.center[1] // TILE_SIZE
        print(self.idx_x, self.idx_y)
        
    def blink(self):
        self.board.red_border(self.idx_x, self.idx_y)
        

#when check the only next moves are to move the king out or
#to move another piece inbetween. But only if that piece you are moving inbetween
#is not already blocking a check move
class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'king', board)
    
    @property   
    def possible_moves(self):
        return [(dx + self.idx_x, dy + self.idx_y) for dx in range(-1, 2) for dy in range(-1, 2)
                 if not(dx == 0 and dy == 0) and (0 <= dx + self.idx_x <= 7) and (0 <= dy + self.idx_y <= 7)]
    
    def calculate_moves(self):
        return [self.check_fields(field) for field in self.possible_moves]
    
    
    def check(self):
        self.board.red_tile(self.idx_x, self.idx_y)
    
    
                     
#only thing left to do here is pawn promotion.

class Pawn(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'pawn', board)
        self.touched = False
            
    @property
    def calculate_capturing_moves(self):
        x, y = self.idx_x, self.idx_y    
        allowed_move1 = x - 1, y - 1 if self.color == 'white' else y + 1  
        allowed_move2 = x + 1, y - 1 if self.color == 'white' else y + 1
        return [allowed_move1, allowed_move2]  
        
    def pick(self):
        self.board.border_tile(self.idx_x, self.idx_y)
        return self.calculate_moves() + self.show_capturing_moves()
    
    def show_capturing_moves(self):
        x, y = self.idx_x, self.idx_y
        move_direction = y - 1 if self.color == 'white' else y + 1
        pos_move1 = self.board.chess_matrix[move_direction][x-1]
        if x + 1 <= 7:
            pos_move2 = self.board.chess_matrix[move_direction][x+1]
        else:
            pos_move2 = None
        allowed_move1 = None
        allowed_move2 = None    
        if isinstance(pos_move1, Piece):
            if pos_move1.color != self.color:
                allowed_move1 = x - 1, y - 1 if self.color == 'white' else y + 1
        if isinstance(pos_move2, Piece):
            if pos_move2.color != self.color:
                allowed_move2 = x + 1, y - 1 if self.color == 'white' else y + 1
        return [allowed_move1, allowed_move2]
    
    def calculate_moves(self):
        x, y = self.idx_x, self.idx_y
        allowed_move1 = x, y+1 if self.color == 'black' else y-1
        blocking_piece = self.board.chess_matrix[allowed_move1[1]][allowed_move1[0]]
        if isinstance(blocking_piece, Piece):
            return [None]
        if self.touched == False:
            allowed_move2 = x, y+2 if self.color == 'black' else y-2
            blocking_piece = self.board.chess_matrix[allowed_move2[1]][allowed_move2[0]]
            if isinstance(blocking_piece, Piece):
                return [allowed_move1]
            return [allowed_move1, allowed_move2]
        return [allowed_move1]
      
           
                    
class Knight(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'knight', board)
        
        
    @property
    def possible_moves(self):
        move_pattern = (( 2 + self.idx_x, self.idx_y + 1),
                        ( 2 + self.idx_x, self.idx_y - 1),
                        (-2 + self.idx_x, self.idx_y + 1),
                        (-2 + self.idx_x, self.idx_y - 1),
                        (-1 + self.idx_x, self.idx_y + 2),
                        ( 1 + self.idx_x, self.idx_y + 2),
                        (-1 + self.idx_x, self.idx_y - 2),
                        ( 1 + self.idx_x, self.idx_y - 2))
        return [(dx, dy) for dx, dy in move_pattern if (0 <= dx <=7 and 0 <= dy <= 7)]
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    def calculate_moves(self):
        return [self.check_fields(field) for field in self.possible_moves]
            
    
class Rook(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'rook', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
    
    @property
    def possible_moves(self): 
        positive_x_moves = 7 - self.idx_x
        positive_y_moves = 7 - self.idx_y
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        limits = [positive_x_moves, self.idx_x, positive_y_moves, self.idx_y]
        
        possible_moves = []
        for (dx, dy), limit in zip(directions, limits):
            for i in range(limit):
                possible_moves.append((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy))
             
        return possible_moves
        
    
    def calculate_moves(self):
        self.active = True   
        possible_moves = []
        
        positive_x_moves = 7 - self.idx_x
        positive_y_moves = 7 - self.idx_y
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        limits = [positive_x_moves, self.idx_x, positive_y_moves, self.idx_y]

        for (dx, dy), limit in zip(directions, limits):
            for i in range(limit):
                if self.active:
                    possible_moves.append(self.check_fields((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy)))
            self.active = True

        return possible_moves
        
    
        
          
class Bishop(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'bishop', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
        
    @property   
    def possible_moves(self):
        possible_moves = []
        positive_x_moves = 7 - self.idx_x
        positive_y_moves = 7 - self.idx_y        
        
        directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        limits = [(positive_x_moves, self.idx_y),
                  (positive_x_moves, positive_y_moves),
                  (self.idx_x, self.idx_y),
                  (self.idx_x, positive_y_moves)]
        

        for (dx, dy), limit in zip(directions, limits):
            for i, _ in zip(range(limit[0]), range(limit[1])):
                possible_moves.append((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy))
                
            
        return possible_moves
        
        
    def calculate_moves(self):
        self.active = True
        possible_moves = []
        positive_x_moves = 7 - self.idx_x
        positive_y_moves = 7 - self.idx_y        
        
        directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        limits = [(positive_x_moves, self.idx_y),
                  (positive_x_moves, positive_y_moves),
                  (self.idx_x, self.idx_y),
                  (self.idx_x, positive_y_moves)]
        

        for (dx, dy), limit in zip(directions, limits):
            for i, _ in zip(range(limit[0]), range(limit[1])):
                if self.active:
                    possible_moves.append(self.check_fields((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy)))
            self.active = True

        return possible_moves
    
    
class Queen(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'queen', board)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    @property
    def possible_moves(self):
        possible_moves = []
        positive_x_moves = 7 - self.idx_x
        positive_y_moves = 7 - self.idx_y        
        
        directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        limits = [(positive_x_moves, self.idx_y),
                  (positive_x_moves, positive_y_moves),
                  (self.idx_x, self.idx_y),
                  (self.idx_x, positive_y_moves)]
        

        for (dx, dy), limit in zip(directions, limits):
            for i, _ in zip(range(limit[0]), range(limit[1])):
                possible_moves.append((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy))
    
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        limits = [positive_x_moves, self.idx_x, positive_y_moves, self.idx_y]
        
        for (dx, dy), limit in zip(directions, limits):
            for i in range(limit):
                possible_moves.append((self.idx_x + (i + 1) * dx, self.idx_y + (i + 1) * dy))
                
        return possible_moves
        
        
    def calculate_moves(self):
        x, y = self.idx_x, self.idx_y
        self.active = True 
        possible_moves = []
        positive_x_moves = 7 - x
        positive_y_moves = 7 - y  
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        limits = [positive_x_moves, x, positive_y_moves, y]

        for (dx, dy), limit in zip(directions, limits):
            for i in range(limit):
                if self.active:
                    possible_moves.append(self.check_fields((x + (i + 1) * dx, y + (i + 1) * dy)))
            self.active = True
        
        directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        limits = [(positive_x_moves, y), (positive_x_moves, positive_y_moves), (x, y), (x, positive_y_moves)]
        
        for (dx, dy), limit in zip(directions, limits):
            for i, _ in zip(range(limit[0]), range(limit[1])):
                if self.active:
                    possible_moves.append(self.check_fields((x + (i + 1) * dx, y + (i + 1) * dy)))
            self.active = True
        
        return possible_moves
