import pygame as pg
import sys
from const import *
from utils import render_letter, get_idx
from board import Board
from player import Player
from pieces import Piece, Pawn, King


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
        self.current_player = 'white'
        self.opp_color = 'black' if self.current_player == 'white' else 'white'
        self.check = False
    
                
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()  
            
            #the next 6 lines are only for debugging purposes
            # king2 = self.board.chess_matrix[7][4]   
            # if isinstance(king2, King):
            #     king2.idx_x = 3
            #     king2.idx_y = 3
            #     king2.assign_pos(king2.idx_x, king2.idx_y)
            #     king2.rect.center = king2.idx_x * TILE_SIZE + TILE_SIZE_05, king2.idx_y * TILE_SIZE + TILE_SIZE_05
            #     self.board.chess_matrix[7][4] = 0
                  
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    pos_idx = get_idx(self.board_pos, pos)
                    self.take_turn(pos_idx, self.current_player)  
                else:
                    self.picked = False
                    self.surface.fill(BOARD_COLOR_1)
                    self.board.draw()  
                    
        
    def take_turn(self, pos_idx, color):
        opp_player = self.player_black if self.current_player == 'white' else self.player_white
        curr_player = self.player_black if self.current_player == 'black' else self.player_white
        if self.picked == False:                    
            self.selected = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
            if isinstance(self.selected, Piece):
                if self.selected.color == color:
                    self.picked = True
                    if self.check == True:
                        if not isinstance(self.selected, King):
                            #only a piece which can kill the self.check_piece or a piece to move inbetween can be selected here
                            #and the only possible move has to be that move.
                            pass
                        else: 
                            self.allowed_moves = self.selected.pick()
                            self.allowed_moves = [move for move in self.allowed_moves if move not in opp_player.kill_moves()]
                                                                  
                    else:    
                        if isinstance(self.selected, King):
                            self.allowed_moves = self.selected.pick()
                            self.allowed_moves = [move for move in self.allowed_moves if move not in opp_player.kill_moves()]
                        else:                                   
                            self.allowed_moves = self.selected.pick()
                            
                    self.current_pos_idx = pos_idx
                    self.board.blink_moves(self.allowed_moves, 'black' if self.current_player == 'white' else 'white') 
        else:                    
            self.move_to = self.board.chess_matrix[pos_idx[1]][pos_idx[0]]
            if pos_idx in self.allowed_moves:
                if isinstance(self.move_to, Piece):
                    if self.move_to.color == 'white' if color == 'black' else 'black':
                        self.move_to.kill()
                        
                self.board.chess_matrix[self.current_pos_idx[1]][self.current_pos_idx[0]] = 0        
                self.selected.rect.center = (pos_idx[0] * TILE_SIZE + TILE_SIZE_05,
                                             pos_idx[1] * TILE_SIZE + TILE_SIZE_05)
                self.selected.assign_pos(pos_idx[1], pos_idx[0])
                self.selected.update_idx()
                self.surface.fill(BOARD_COLOR_1)
                self.board.draw()
                self.picked = False
                self.check = False
                self.current_player = 'black' if self.current_player == 'white' else 'white'    
                if isinstance(self.selected, Pawn):
                    self.selected.touched = True  
                next_move = self.selected.calculate_next_move()
                for move in next_move:
                    if move != None:
                        x, y = move
                        if isinstance(self.board.chess_matrix[y][x], King):
                            self.check = True
                            self.king = self.board.chess_matrix[y][x]
                            #the index of the self.check_piece is gonna be important
                            #need to use it in a method in the player class
                            self.check_piece = self.selected
                kill_moves = curr_player.kill_moves()
                print(kill_moves)
                if (opp_player.king.idx_x, opp_player.king.idx_y) in kill_moves:
                    #we need a dict here to solve the problem that the self.check_piece 
                    #has to be determined. Something like this {piece: [*kill_moves], ...}
                    #also check_piece in this particular case can only be Queen, Rook or Bishop.
                    self.check = True
                    self.king = opp_player.king
                
                
                                                                
    def draw_symbols(self):
        for i in range(2):
            for pos in XY_POS[i]:   
                for j, number in enumerate(SYMBOLS[i]):
                    render_letter(self.font, number, self.screen, 
                                  (pos, SOME_MORE_SPACE // 2 + TILE_SIZE_05 + j * TILE_SIZE)
                                   if i == 0 else (SOME_MORE_SPACE // 2 + TILE_SIZE_05 + j * TILE_SIZE, pos)) 
        
    def update(self):
        self.clock.tick(FPS)              
        self.draw()     
        
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.surface, (self.board_pos))
        self.player_black.draw()
        self.player_white.draw()
        self.draw_symbols()
        if self.check:
            self.check_piece.blink()
            self.board.black_tile(self.king.idx_x, self.king.idx_y)
        pg.display.flip()          
            
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            pg.display.update() 
            
    
if __name__ == '__main__':
    game = App(WIN_SIZE)
    game.run()