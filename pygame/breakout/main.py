import pygame as pg
import sys, os
import time
from settings import *
from sprites import Player

class Game:
    def __init__(self, W_SIZE=RES):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption('Breakout')
        self.bg = self.get_scaled_image(path='src/graphics/other/bg.png', res=RES)
        
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self.all_sprites)
        
        
    @staticmethod
    def get_scaled_image(path, res):
        cwd = os.path.dirname(os.path.abspath(__file__))
        img = pg.image.load(os.path.join(cwd, path)).convert()
        scale_factor = HEIGHT / img.get_height()
        scaled_width = img.get_width() * scale_factor
        scaled_height = img.get_height() * scale_factor
        return pg.transform.smoothscale(img, (scaled_width, scaled_height))
    
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            
                
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.all_sprites.draw(self.screen)
    
    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()
            self.input(pg.event.get())
            self.draw()
            pg.display.update()
            self.player.update(dt)  
    
if __name__ == '__main__':
    game = Game()
    game.run()