import sys 
import pygame as pg
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('App')
        self.screen  = pg.display.set_mode(RES)
        self.clock   = pg.time.Clock()
        self.sprites = pg.sprite.Group()
        self.obj     = Object(self.sprites)
        pg.time.set_timer(TIMER_EVENT, ANIM_TIME_INTERVAL)
        

    def update(self):
        self.clock.tick(FPS) 
    
    def draw(self):
        self.screen.fill(FIELD_COLOR)
        self.sprites.draw(self.screen)
        pg.display.flip() 

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
            
            
class Object(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pg.Surface((50, 80))
        self.rect = self.image.get_rect(topleft=(WIDTH // 2, HEIGHT //2))
        self.image.fill('black')
        
    
        
            
            
print(TIMER_EVENT)            
if __name__ == '__main__':
    app = App()
    app.run()