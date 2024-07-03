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
           
    def assign_pos(self, x, y):
        self.board.chess_matrix[x][y] = self
        
        
    def show_capture(self, x, y, color):
        return [None]
                     
                    

class Queen(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'queen', board)
        
    def pick(self, x, y, player):
        self.board.border_tile(x, y)
        return [None]  
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
          
#checkmate and stalemate left here 
class King(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'king', board)
        
    def pick(self, x, y, player):
        self.board.border_tile(x, y)
        allowed_moves = self.calculate_moves(x, y)
        actual_allowed_moves = []
        for coords in allowed_moves:
            try:
                blocking_piece = self.board.chess_matrix[coords[1]][coords[0]]
            except IndexError:
                blocking_piece = None
            if not(isinstance(blocking_piece, Piece)):
                self.board.blink_tile(*coords)
                actual_allowed_moves.append(coords)
        return actual_allowed_moves
    
    def show_capture(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        possible_moves = self.calculate_moves(x, y)
        kill_moves = [None]
        for coords in possible_moves:
            try:
                enemy_piece = self.board.chess_matrix[coords[1]][coords[0]]
            except IndexError:
                enemy_piece = None
            if isinstance(enemy_piece, Piece):
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
        
    def pick(self, x, y, player):
        self.board.border_tile(x, y)
        allowed_move1 = x, y+1 if self.color == 'black' else y-1
        blocking_piece = self.board.chess_matrix[allowed_move1[1]][allowed_move1[0]]
        if isinstance(blocking_piece, Piece):
            return [None]
        
        self.board.blink_tile(*allowed_move1)
        self.picked = True
        if self.touched == False:
            allowed_move2 = x, y+2 if self.color == 'black' else y-2
            blocking_piece = self.board.chess_matrix[allowed_move2[1]][allowed_move2[0]]
            if isinstance(blocking_piece, Piece):
                return [allowed_move1]
            self.board.blink_tile(*allowed_move2)
            return allowed_move1, allowed_move2
        return [allowed_move1]
    
    def show_capture(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        move_direction = y - 1 if player == 0 else y + 1
        pos_move1 = self.board.chess_matrix[move_direction][x-1]
        if x+1 <= 7:
            pos_move2 = self.board.chess_matrix[move_direction][x+1]
        else:
            pos_move2 = None
        allowed_move1 = None
        allowed_move2 = None    
        if isinstance(pos_move1, Piece):
            if pos_move1.color == opp_color:
                allowed_move1 = x - 1, y - 1 if player == 0 else y + 1
                self.board.red_tile(*allowed_move1)
        if isinstance(pos_move2, Piece):
            if pos_move2.color == opp_color:
                allowed_move2 = x + 1, y - 1 if player == 0 else y + 1
                self.board.red_tile(*allowed_move2)
        return allowed_move1, allowed_move2
                        
class Knight(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'knight', board)
        
    def pick(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        allowed_moves = [None]
        self.board.border_tile(x, y)
        moves = self.calculate_moves(x, y)
        
        for coords in moves:
            try:
                blocking_piece = self.board.chess_matrix[coords[1]][coords[0]]
            except IndexError:
                blocking_piece = None
            if isinstance(blocking_piece, Piece):
                if blocking_piece.color == opp_color:
                    self.board.red_tile(*coords)
                    allowed_moves.append(coords)
            else:
                self.board.blink_tile(*coords) 
                allowed_moves.append(coords)
                      
        print(allowed_moves)
        return allowed_moves
                
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
        
    calculate_moves = lambda self, x, y: [(dx, dy) for dx, dy in (( 2 + x, y + 1),
                                                                  ( 2 + x, y - 1),
                                                                  (-2 + x, y + 1), 
                                                                  (-2 + x, y - 1),
                                                                  (-1 + x, y + 2),
                                                                  ( 1 + x, y + 2), 
                                                                  (-1 + x, y - 2), 
                                                                  ( 1 + x, y - 2))  
                                                    if (0 <= dx <=7 and 0 <= dy <= 7)]
        
    
class Rook(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'rook', board)
        
    def pick(self, x, y, player):
        self.board.border_tile(x, y)
        possible_moves = self.calculate_moves(x, y, player)
        return possible_moves
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
    
    def check_fields(self, field, opp_color):
        moves = []
        field_obj = self.board.chess_matrix[field[1]][field[0]]
        if isinstance(field_obj, Piece):
            if field_obj.color == opp_color:
                self.board.red_tile(*field)
                moves.append(field)
                self.d = None
            else:
                self.d = None
        else:
            moves.append(field)
            self.board.blink_tile(*field)
        return moves
    
    #if you know a way to write these 4 while statements in a loop please let me know.
    def calculate_moves(self, x, y, player):
        opp_color = 'black' if player == 0 else 'white'
        pos_moves = []
        self.d = 1   
                
        while self.d != None and 7 >= x + self.d:
            field = x + self.d, y
            self.d += 1
            pos_moves.extend(self.check_fields(field, opp_color))    
        self.d = 1
          
        while self.d != None and 0 <= x - self.d:
            field = x - self.d, y
            self.d += 1
            pos_moves.extend(self.check_fields(field, opp_color))
        self.d = 1
                        
        while self.d != None and 7 >= y + self.d:
            field = x, y + self.d
            self.d += 1
            pos_moves.extend(self.check_fields(field, opp_color))
        self.d = 1
            
        while self.d != None and 0 <= y - self.d:
            field = x, y - self.d
            self.d += 1
            pos_moves.extend(self.check_fields(field, opp_color))
        self.d = 1
            
        return pos_moves
        
          
class Bishop(Piece):
    def __init__(self, x, y, color, board):
        super().__init__(x, y, color, 'bishop', board)
        
    def pick(self, x, y, player):
        self.board.border_tile(x, y)
        return [None]
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 
