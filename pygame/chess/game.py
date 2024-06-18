import pygame as pg
import sys, os
from const import *
from objects import Piece
from board import Board
from player import Player


class Game:
    def __init__(self, W_SIZE):
        pg.init()
        self.screen = pg.display.set_mode(W_SIZE)
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()     
        self.board = Board(self)
        self.piece = Piece(self, 32, 32, 'black', TYPES[0])
        self.player_white = Player('white')
        self.player_black = Player('black')
        self.sprites.add(self.piece)
        self.pawns = self.draw_pieces('black', 'pawn')
        
        for pawn in self.pawns:
            print(pawn.rect.topleft, pawn.rect.bottomright)
                         
    def draw_pieces(self, color, type_):
        pieces = pg.sprite.Group()
        for i in range(32, WIDTH, 64):
            piece = Piece(self, i, TILE_SIZE + TILE_SIZE // 2, color, type_)
            pieces.add(piece)
        return pieces
        

    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def update(self):
        self.clock.tick(FPS)                   
        self.draw()
        self.sprites.update()
        self.pawns.update            
    
                
    def draw(self):
        self.screen.fill(BOARD_COLOR_1)
        self.board.draw()
        self.sprites.draw(self.screen)
        self.pawns.draw(self.screen)
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.draw()
            pg.display.update()    
    
if __name__ == '__main__':
    game = Game(WIN_SIZE)
    game.run()