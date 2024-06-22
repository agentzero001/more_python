import pygame as pg
import sys, os
from const import *
from utils import render_letter
from board import Board
from player import Player


class App:
    def __init__(self, W_SIZE):
        pg.init()
        self.screen = pg.display.set_mode(W_SIZE)
        self.surface = pg.Surface((WIDTH, HEIGHT))
        self.surface.fill(BOARD_COLOR_1)
        self.clock = pg.time.Clock() 
        self.font = pg.font.Font(None, 40)
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
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.surface, ([SOME_MORE_SPACE // 2] * 2))
        self.board.draw()
        self.player_black.draw()
        self.player_white.draw()
        for i, letter in enumerate('ABCDEFGH'):
            render_letter(self.font, letter, self.screen,
                          (SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE,
                           SOME_MORE_SPACE // 2 + HEIGHT + TILE_SIZE_05))
            
        for i, number in enumerate(range(8, 0, -1)):
            render_letter(self.font, number, self.screen, 
                          (SOME_MORE_SPACE // 2 - TILE_SIZE_05,
                           SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE))       
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            pg.display.update()    
    
if __name__ == '__main__':
    game = App(WIN_SIZE)
    game.run()