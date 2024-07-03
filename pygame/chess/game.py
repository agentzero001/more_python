import pygame as pg
import sys
from const import *
from utils import render_letter, get_idx
from board import Board
from player import Player
from pieces import Piece


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
                
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            #these 3 lines exist only for a debugging purpose
            # cur_pos = pg.mouse.get_pos()
            # x, y = get_idx(self.board_pos, cur_pos)
            # print(self.board.chess_matrix[y][x])
            
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    pos_idx = get_idx(self.board_pos, pos)
                    if self.picked == False:                    
                        self.selected = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
                        if isinstance(self.selected, Piece):
                            color = 'white' if self.current_player == 0 else 'black'
                            if self.selected.color == color:
                                self.picked = True
                                self.allowed_moves = list(self.selected.pick(*pos_idx, self.current_player))
                                self.allowed_moves.extend(self.selected.show_capture(*pos_idx, self.current_player))
                                self.current_pos_idx = pos_idx
                    else:
                        if hasattr(self.selected, 'touched'):
                            self.selected.touched = True
        
                        self.move_to = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
                        if pos_idx in self.allowed_moves:
                            if isinstance(self.move_to, Piece):
                                if self.move_to.color == 'white' if self.current_player == 1 else 'black':
                                    self.move_to.kill()
                                    
                            self.board.chess_matrix[self.current_pos_idx[1]][self.current_pos_idx[0]] = 0        
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
        
        
    def draw_symbols(self):
        for i in range(2):
            for pos in XY_POS[i]:   
                for j, number in enumerate(SYMBOLS[i]):
                    render_letter(self.font, number, self.screen, 
                                  (pos, SOME_MORE_SPACE // 2 + TILE_SIZE_05 + j * TILE_SIZE)
                                   if i == 0 else (SOME_MORE_SPACE // 2 + TILE_SIZE_05 + j * TILE_SIZE, pos)) 
        
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.surface, (self.board_pos))
        self.player_black.draw()
        self.player_white.draw()
        self.draw_symbols()
        pg.display.flip()       
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            pg.display.update() 
            
    
if __name__ == '__main__':
    game = App(WIN_SIZE)
    game.run()