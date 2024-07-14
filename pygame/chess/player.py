import pygame as pg
from const import *
from pieces import *

class Player:
    def __init__(self, app, board, color):
        self.app = app
        self.board = board
        self.pawns = self.draw_pawns(color)
        self.pieces = [piece(TILE_SIZE * x_pos + TILE_SIZE_05,
                             TILE_SIZE * 7 + TILE_SIZE_05 if color == 'white' else TILE_SIZE_05,
                             color,
                             self.board) 
                        for piece, x_pos in zip([Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], range(8))] 
        self.piece_group = pg.sprite.Group()
        self.piece_group.add(*self.pieces)      
                   
    def draw_pawns(self, color):
        pawns = pg.sprite.Group()
        if color == 'black':
            for i in range(TILE_SIZE_05, WIDTH, 64):
                piece = Pawn(i, TILE_SIZE + TILE_SIZE // 2, color, self.board)
                pawns.add(piece)
        else:
            for i in range(TILE_SIZE_05, WIDTH, 64):
                piece = Pawn(i , TILE_SIZE * 6 + TILE_SIZE // 2, color, self.board)
                pawns.add(piece)
        return pawns
    
    def update(self):
        self.pawns.update()
        self.piece_group.update()   
        
    def draw(self):
        self.pawns.draw(self.app.surface)
        self.piece_group.draw(self.app.surface)
        
    def kill_moves(self):
        kill_moves = []
        for piece in self.piece_group:
            kill_moves += piece.calculate_next_move()
            
        for pawn in self.pawns:
            kill_moves += pawn.calculate_capturing_moves()
            
        return kill_moves
            
        
        
    # def take_turn(self, pos_idx):
    #     color = self.color
    #     if self.picked == False:                    
    #         self.selected = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
    #         if isinstance(self.selected, Piece):
    #             if self.selected.color == color:
    #                 self.picked = True
    #                 self.allowed_moves = list(self.selected.pick())
    #                 self.current_pos_idx = pos_idx
    #     else:                    
    #         self.move_to = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
    #         if pos_idx in self.allowed_moves:
    #             if isinstance(self.move_to, Piece):
    #                 if self.move_to.color == 'white' if color == 'black' else 'black':
    #                     self.move_to.kill()
                        
    #             self.board.chess_matrix[self.current_pos_idx[1]][self.current_pos_idx[0]] = 0        
    #             self.selected.rect.center = (pos_idx[0] * TILE_SIZE + TILE_SIZE_05,
    #                                          pos_idx[1] * TILE_SIZE + TILE_SIZE_05)
    #             self.selected.assign_pos(pos_idx[1], pos_idx[0])
    #             self.selected.update_idx()
    #             self.surface.fill(BOARD_COLOR_1)
    #             self.board.draw()
    #             self.picked = False
    #             self.current_player = 'black' if self.current_player == 'white' else 'white'    
    #             if isinstance(self.selected, Pawn):
    #                 self.selected.touched = True  
    #             next_move = self.selected.calculate_next_move()
    #             for move in next_move:
    #                 if move != None:
    #                     x, y = move
    #                     position = self.board.chess_matrix[y][x]
    #                     if isinstance(position, King):
    #                         self.board.red_border(pos_idx[0], pos_idx[1])
    #                         position.check()