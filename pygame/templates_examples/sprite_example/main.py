import sys 
import pygame as pg
from sprite import Object, Square
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('App')
        self.screen  = pg.display.set_mode(RES)
        self.clock   = pg.time.Clock()
        #self.obj     = Object(self.sprites)
        self.square  = Square('crimson', 500, 300)
        self.sprites = pg.sprite.Group(self.square)    

    def update(self):
        self.clock.tick(FPS) 
        self.draw()
        #self.square.update()  #the sprites.update is alrdy calling the Square update method
        self.sprites.update()
        
    def draw(self):
        self.screen.fill(FIELD_COLOR)
        self.sprites.draw(self.screen)

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                self.square = Square('black', pos[0], pos[1])
                self.sprites.add(self.square)
                print(pg.mouse.get_rel())      
                
    def run(self):
        while True:
            print(self.sprites)
            self.check_events()
            self.update()
            pg.display.flip()            

        
           
if __name__ == '__main__':
    app = App()
    app.run()
    