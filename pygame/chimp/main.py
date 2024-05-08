#todo: modify chimp.py such that it is more readable
import os
import sys
import pygame as pg
from game_objects import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Monkey Fever")
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((1280, 480), pg.SCALED)
        self.bg = pg.Surface(self.screen.get_size())
        self.bg = self.bg.convert()
        self.font = pg.font.Font(None, 64)
        self.text = self.font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
        self.textpos = self.text.get_rect(centerx=self.bg.get_width() / 2, y=10)
        self.chimp = Chimp()
        self.fist = Fist()
        self.clock = pg.time.Clock()
        self.allsprites = pg.sprite.RenderPlain((self.chimp, self.fist))
        self.whiff_sound = load_sound("whiff.wav")
        self.punch_sound = load_sound("punch.wav")
        self.bg.fill((170, 238, 187))
        self.bg.blit(self.text, self.textpos)
        
        
    def input(self, events): 
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()  
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.fist.punch(self.chimp):
                    self.punch_sound.play()
                    self.chimp.punched()
                else:
                    self.whiff_sound.play()  
            elif event.type == pg.MOUSEBUTTONUP:
                self.fist.unpunch()  
    
    def update(self):
        self.clock.tick(60)
        self.allsprites.update()
        pg.display.flip()
    
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.allsprites.draw(self.screen)
    
    def run(self):
        while True:
            self.input(pg.event.get())
            self.update()
            self.draw()
    
if __name__ == '__main__':
    game = App()
    game.run()
        
