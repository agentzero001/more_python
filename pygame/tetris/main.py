import pygame as pg
from tetris import Tetris
from settings import *


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        #self.TILE_SIZE = self.W_SIZE // 20
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)
        self.new_game()
        
    def new_game(self):
        pass
    
    
    def update(self):
        self.clock.tick(FPS)
    
    def draw_grid(self):
        tuple(pg.draw.line(self.screen,
                           (40,) * 3,
                           (x, 0),
                           (x, self.W_SIZE))
              for x in range(0,
                             self.W_SIZE,
                             self.TILE_SIZE))
        
        tuple(pg.draw.line(self.screen,
                           (40,) * 3,
                           (0, y),
                           (self.W_SIZE, y))
              for y in range(0,
                             self.W_SIZE,
                             self.TILE_SIZE))

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                #sys.exit()  

    def draw(self):
            self.screen.fill(FIELD_COLOR)
            pg.display.flip()
            self.tetris.draw()
            #self.draw_grid()


    def run(self):
            while True:
                self.draw()
                self.check_events()
                self.update()
                
if __name__ == '__main__':
    app = App()
    app.run()