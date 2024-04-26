import pygame as pg
from settings import *
from scene import Scene
import sys

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True
        self.scene = Scene(self)
                
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False         
                
    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.close()
        
    def draw(self):
        self.scene.draw()
    
    def update(self):
        self.scene.update()
        pg.display.update()
        
    def close(self):
        pg.quit()
        sys.exit()
                   
            
        
if __name__ == '__main__':
    app = Game()
    app.run()