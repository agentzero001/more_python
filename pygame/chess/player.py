import pygame as pg
from const import *
from pieces import *

class Player:
    def __init__(self, app,  board, color):
        self.app = app
        self.board = board
        self.pawns = self.draw_pawns(color)
        if color == 'white':
            self.king = King(TILE_SIZE * 4 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.queen = Queen(TILE_SIZE * 3 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.knight1 = Knight(TILE_SIZE + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.knight2 = Knight(TILE_SIZE * 6 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.rook1 = Rook(TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.rook2 = Rook(TILE_SIZE * 7 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.bishop1 = Bishop(TILE_SIZE * 2 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
            self.bishop2 = Bishop(TILE_SIZE * 5 + TILE_SIZE_05, TILE_SIZE * 7 + TILE_SIZE_05, color, self.board)
        else:
            self.king = King(TILE_SIZE * 4 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.queen = Queen(TILE_SIZE * 3 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.knight1 = Knight(TILE_SIZE + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.knight2 = Knight(TILE_SIZE * 6 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.rook1 = Rook(TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.rook2 = Rook(TILE_SIZE * 7 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.bishop1 = Bishop(TILE_SIZE * 2 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            self.bishop2 = Bishop(TILE_SIZE * 5 + TILE_SIZE_05, TILE_SIZE_05, color, self.board)
            
                   
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
        self.king.draw(self.app.surface)
        self.queen.draw(self.app.surface)
        self.knight1.draw(self.app.surface)
        self.knight2.draw(self.app.surface)
        self.rook1.draw(self.app.surface)
        self.rook2.draw(self.app.surface)
        self.bishop1.draw(self.app.surface)
        self.bishop2.draw(self.app.surface)
        