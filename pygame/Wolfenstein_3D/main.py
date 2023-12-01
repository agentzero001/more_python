import sys 
import pygame as pg
from settings import *
import map_ as m

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        

    def new_game(self):
        self.map1 = m.Map(self)

    def update(self):
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS) 
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    
    def draw(self):
        self.screen.fill('black')
        self.map1.draw()    
 
    def check_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:
                self.anim_trigger = True
                
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
                      
if __name__ == '__main__':
    app = Game()
    app.run()