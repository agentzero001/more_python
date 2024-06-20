import pygame as pg
import sys, os
from const import *
from board import Board
from player import Player


class Game:
    def __init__(self, W_SIZE):
        pg.init()
        self.screen = pg.display.set_mode(W_SIZE)
        self.clock = pg.time.Clock()     
        self.board = Board(self)
        self.player_white = Player(self, 'white')
        self.player_black = Player(self, 'black')      
        
        for pawn in self.player_black.pawns:
            print(pawn.rect.topleft, pawn.rect.bottomright)
                         
        
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def update(self):
        self.clock.tick(FPS)                   
        self.draw()                   
                
    def draw(self):
        self.screen.fill(BOARD_COLOR_1)
        self.board.draw()
        self.player_black.draw()
        self.player_white.draw()
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            pg.display.update()    
    
if __name__ == '__main__':
    game = Game(WIN_SIZE)
    game.run()