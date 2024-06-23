import pygame as pg
from const import *
from pieces import *

class Player:
    def __init__(self, app,  board, color):
        self.app = app
        self.board = board
        self.pawns = self.draw_pawns(color)
        self.pieces = []
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Rook, Knight]
        y_pos = TILE_SIZE * 7 + TILE_SIZE_05 if color == 'white' else TILE_SIZE_05
        for piece, x_pos in zip(pieces, range(8)):
            p = piece(TILE_SIZE * x_pos + TILE_SIZE_05, y_pos, color, self.board)
            self.pieces.append(p)
            
            
                   
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
        
    def draw(self):
        self.pawns.draw(self.app.surface)
        for piece in self.pieces:
            piece.draw(self.app.surface)       