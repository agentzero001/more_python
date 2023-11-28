import sys 
import pygame as pg
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('App')
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def update(self):
        self.clock.tick(FPS) 
    
    def draw(self):
        self.screen.fill(FIELD_COLOR)
        pg.display.flip() 

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
            
if __name__ == '__main__':
    app = App()
    app.run()