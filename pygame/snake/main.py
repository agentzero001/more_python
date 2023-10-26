import pygame as pg
from game_objects import *

W_SIZE = 600

class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode([W_SIZE] * 2)
        self.clock = pg.time.Clock()
        
    def new_game(self):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def check_events(self):
        pass
    
    def run(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    game = Game()
    game.run()