import pygame as pg
import sys, os
from const import *
from pygame.math import Vector2 as V
from utils import render_letter, get_idx
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
        self.board_pos = ([SOME_MORE_SPACE // 2] * 2)
        self.player_white = Player(self, self.board, 'white')
        self.player_black = Player(self, self.board, 'black')
        self.board.draw()
        self.picked = False
        self.current_player = 0
        self.selected = 0
            
        # for pawn in self.player_black.pawns:
    
    #     print(pawn.rect.topleft, pawn.rect.bottomright)                         
        
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    pos_idx = get_idx(self.board_pos, pos)
                    if self.picked == False:                    
                        self.selected = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
                        if hasattr(self.selected, 'color'):
                            color = 'white' if self.current_player == 0 else 'black'
                            if self.selected.color == color:
                                self.picked = True
                                self.selected.pick(*pos_idx) 
                    else:
                        if hasattr(self.selected, 'touched'):
                            self.selected.touched = True
                        self.selected.rect.center = (pos_idx[0] * TILE_SIZE + TILE_SIZE_05,
                                                     pos_idx[1] * TILE_SIZE + TILE_SIZE_05)
                        self.selected.assign_pos(pos_idx[1], pos_idx[0])
                        self.surface.fill(BOARD_COLOR_1)
                        self.board.draw()
                        self.picked = False
                        self.current_player = 1 if self.current_player == 0 else 0
                        
                else:
                    self.picked = False
                    self.surface.fill(BOARD_COLOR_1)
                    self.board.draw() 
                      
    def update(self):
        self.clock.tick(FPS)                   
        self.draw()                   
                
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.surface, (self.board_pos))
        self.player_black.draw()
        self.player_white.draw()
        for i, letter in enumerate('ABCDEFGH'):
            render_letter(self.font, letter, self.screen,
                          (SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE,
                           SOME_MORE_SPACE // 2 + HEIGHT + TILE_SIZE_05))
            
        for i, letter in enumerate('ABCDEFGH'):
            render_letter(self.font, letter, self.screen,
                          (SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE,
                           SOME_MORE_SPACE // 2 - TILE_SIZE_05))
            
        for i, number in enumerate(range(8, 0, -1)):
            render_letter(self.font, number, self.screen, 
                          (SOME_MORE_SPACE // 2 - TILE_SIZE_05,
                           SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE))
            
        for i, number in enumerate(range(8, 0, -1)):
            render_letter(self.font, number, self.screen, 
                          (SOME_MORE_SPACE // 2 + WIDTH + TILE_SIZE_05,
                           SOME_MORE_SPACE // 2 + TILE_SIZE_05 + i * TILE_SIZE))  
            
        pg.display.flip()       
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            print(self.picked)
            pg.display.update() 
            
    
if __name__ == '__main__':
    game = App(WIN_SIZE)
    game.run()