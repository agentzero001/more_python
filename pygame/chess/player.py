import pygame as pg
from const import *
from pieces import *

class Player:
    def __init__(self, app,  board, color):
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