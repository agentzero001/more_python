import pygame as pg
from tetris import Tetris
from settings import *


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)
        #self.new_game()
        
    def new_game(self):
        pass
    
    def update(self):
        self.clock.tick(FPS)
    
    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                #sys.exit()  

    def draw(self):
            self.screen.fill(FIELD_COLOR)
            self.tetris.draw()
            pg.display.flip()

    def run(self):
            while True:
                self.draw()
                self.check_events()
                self.update()
                
if __name__ == '__main__':
    app = App()
    app.run()