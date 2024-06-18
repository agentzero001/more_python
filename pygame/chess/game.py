import pygame as pg
import sys, os
from const import *
from objects import Piece
from board import Board


class Game:
    def __init__(self, W_SIZE):
        pg.init()
        self.screen = pg.display.set_mode(W_SIZE)
        self.clock = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        #self.bg = get_scaled_image(path='assets/board.png', res = (W_SIZE-100,) * 2)
        self.board = Board(self)
        self.piece = Piece(self, 32, 32)
        self.sprites.add(self.piece)
                

    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
    def update(self):
        self.clock.tick(FPS)                   
        self.draw()
        self.sprites.update()            
    
                
    def draw(self):
        self.screen.fill((20,20,20))
        self.board.draw()
        self.sprites.draw(self.screen)
    
    def run(self):
        while True:
            self.input(pg.event.get())
            self.draw()
            pg.display.update()    
    
if __name__ == '__main__':
    game = Game(WIN_SIZE)
    game.run()