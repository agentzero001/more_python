import sys 
import pygame as pg
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
                
    def run(self):
        while True:
            print(self.sprites)
            self.check_events()
            self.update()
            pg.display.flip() 
            
            
class Object(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pg.Surface((50, 80))
        self.rect = self.image.get_rect(topleft=(WIDTH // 2, HEIGHT //2))
        self.image.fill('black')
        
   
class Square(pg.sprite.Sprite):
    def __init__(self, col, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
                
        
    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.kill()
        
           
if __name__ == '__main__':
    app = App()
    app.run()
    