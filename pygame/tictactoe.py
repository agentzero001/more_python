import pygame as pg
import sys
from random import randint

class Tictactoe:
    def __init__(self, game):
        pass
        




class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode([W_SIZE] * 2)
        self.clock = pg.time.Clock()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.screen.fill((20, 20, 20))
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
    