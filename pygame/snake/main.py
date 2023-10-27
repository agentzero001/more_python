import pygame as pg
import sys
from game_objects import *

class Game:
    def __init__(self, W_SIZE=800):
        pg.init()
        self.W_SIZE = W_SIZE
        self.TILE_SIZE = self.W_SIZE // 20
        self.screen = pg.display.set_mode([self.W_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.new_game()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                #sys.exit()

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)
    
    def update(self):
        pg.display.flip()
        self.clock.tick(60)

    def draw_grid(self):
        tuple(pg.draw.line(self.screen,
                           (50,) * 3,
                           (x, 0),
                           (x, self.W_SIZE))
              for x in range(0,
                             self.W_SIZE,
                             self.TILE_SIZE))
        
        tuple(pg.draw.line(self.screen,
                           (50,) * 3,
                           (0, y),
                           (self.W_SIZE, y))
              for y in range(0,
                             self.W_SIZE,
                             self.TILE_SIZE))
        
        
    def draw(self):
        self.screen.fill('black')
        self.draw_grid()
        self.snake.draw()
        self.snake.update()
        #self.food.draw()
        
        
    def run(self):
        while True:
            self.draw()
            self.check_events()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()