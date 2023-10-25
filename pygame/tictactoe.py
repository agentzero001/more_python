import pygame as pg
import sys
from random import randint

class Tictactoe:
    def __init__(self, game, W_SIZE, screen):
        self.LINE_COLOR = (80, 80, 80)
        self.W_SIZE = W_SIZE
        self.screen = screen
        self.board = [['' for i in range(3)] for j in range(3)]
        self.GREY = (80,80,80)
        self.OBJ_SIZE = 60
        self.OBJ_WIDTH = 15
        self.GRID_SIZE = 3
       
    
    def run(self):
        self.board[0][0] = 'O'
        
        for x in range(1,3):
            pg.draw.line(self.screen, self.LINE_COLOR, (50, x*200), (self.W_SIZE - 50, x*200), 5)
            pg.draw.line(self.screen, self.LINE_COLOR, (x*200, 50), (x*200, self.W_SIZE - 50), 5)
            
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                if self.board[row][col] == 'X':
                    x = col * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    y = row * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    pg.draw.line(self.screen, self.GREY, (x - self.OBJ_SIZE, y - self.OBJ_SIZE), (x + self.OBJ_SIZE, y + self.OBJ_SIZE), self.OBJ_WIDTH)
                    pg.draw.line(self.screen, self.GREY, (x - self.OBJ_SIZE, y + self.OBJ_SIZE), (x + self.OBJ_SIZE, y - self.OBJ_SIZE), self.OBJ_WIDTH)
                elif self.board[row][col] == 'O':
                    x = col * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    y = row * self.W_SIZE // self.GRID_SIZE + self.W_SIZE // (2 * self.GRID_SIZE)
                    pg.draw.circle(self.screen, self.GREY, (x, y), self.OBJ_SIZE, self.OBJ_WIDTH)
   
            
class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode([W_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = Tictactoe(self, W_SIZE, self.screen)
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.screen.fill((20, 20, 20))
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
    