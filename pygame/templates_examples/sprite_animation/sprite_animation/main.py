import sys 
import pygame as pg
from sprite import Player
from settings import *
import os

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('App')
        self.screen  = pg.display.set_mode(RES)
        self.clock   = pg.time.Clock()
        self.sprites = pg.sprite.Group() 
        self.player = Player(self, WIDTH//2, HEIGHT//2)
        self.sprites.add(self.player)
        # for i in range(11):
        #     self.square  = Player(self, i*100, HEIGHT //2, i)
        #     self.sprites.add(self.square)
         
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.player.defend_trigger = True  
                if event.key == pg.K_s:
                    self.player.attack_trigger = True
                    
    def run(self):
        while True:
            self.check_events()
            self.update()
            pg.display.flip()            
          
           
if __name__ == '__main__':
    app = App()
    app.run()
    