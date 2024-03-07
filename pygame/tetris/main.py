import pygame as pg
from tetris import Tetris
from settings import *
import sys


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris')
        self.screen     = pg.display.set_mode(WIN_RES)
        self.clock      = pg.time.Clock()
        self.tetris     = Tetris(self)
        self.menu       = Menu(self)
        self.start_game = False
        pg.time.set_timer(pg.USEREVENT, ANIM_TIME_INTERV)
        pg.time.set_timer(pg.USEREVENT+1, FAST_ANIM_TIME_INT)
    
    def new_game(self):
        self.tetris     = Tetris(self)
        self.start_game = False
    
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS) 
        
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.screen.fill(color = FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        pg.display.flip()  
    
    def check_events(self):
        self.anim_trigger = False
        self.anim_trigger_f = False
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()  
            elif event.type == pg.KEYDOWN:
                self.tetris.control(event.key)
                if event.key == pg.K_SPACE:
                    self.start_game = True           
            elif event.type == pg.USEREVENT:
                self.anim_trigger = True
            elif event.type == pg.USEREVENT+1:
                self.anim_trigger_f = True
                

    def run(self):
        while True:
            self.check_events()
            if self.start_game:
                self.update()
                self.draw()
            else:
                self.menu.draw()
            

class Menu:
    def __init__(self, app):
        self.app          = app
        self.font         = pg.font.SysFont(None, 20)
        self.text_surface = self.font.render('press space to start game', True, 'grey')
        self.surface      = pg.Surface((WIN_RES[0] // 1.2, WIN_RES[1] // 4))
        self.x            = (WIN_RES[0] - WIN_RES[0] // 1.2) // 2
        self.y            = (WIN_RES[1] - WIN_RES[1] // 4) // 2
        self.text_x       = (self.surface.get_width() - self.text_surface.get_width()) // 2
        self.text_y       = (self.surface.get_height() - self.text_surface.get_height()) // 2
        self.surface.blit(self.text_surface, (self.text_x, self.text_y))
        
    def draw(self):
        self.app.screen.fill((50,50,50))
        self.app.screen.blit(self.surface, (self.x, self.y))
        pg.display.flip()
        
                        
app = App()
app.run()