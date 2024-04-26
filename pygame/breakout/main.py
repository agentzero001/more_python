import pygame as pg
import sys
import os
import time
from settings import *
from sprites import Player, Ball, Blocks


class Game:
    def __init__(self, W_SIZE=RES):
        pg.init()
        pg.display.set_caption('Breakout')
        self.screen  = pg.display.set_mode(RES)
        self.clock   = pg.time.Clock()
        self.bg      = self.get_scaled_image(path='src/graphics/other/bg.png', res=RES)
        self.sprites = pg.sprite.Group()
        self.player  = Player(self.sprites)
        self.ball    = Ball(self.sprites, self.player)
        
        self.block_group = pg.sprite.Group()
        self.blocks = [Blocks(self.block_group, self.ball, *xy) for xy in BLOCK_COORDS]
        
        
    @staticmethod
    def get_scaled_image(path, res):
        cwd = os.path.dirname(os.path.abspath(__file__))
        img = pg.image.load(os.path.join(cwd, path)).convert()
        scale_factor  = HEIGHT / img.get_height()
        scaled_width  = img.get_width() * scale_factor
        scaled_height = img.get_height() * scale_factor
        return pg.transform.smoothscale(img, (scaled_width, scaled_height))

    def input(self, events):
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.ball.active = True  

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.sprites.draw(self.screen)
        self.block_group.draw(self.screen)
        
    def update(self, dt):
        self.delta_time = self.clock.tick(144)
        pg.display.update()
        self.player.update(self.delta_time)
        self.ball.update(self.delta_time)
        self.block_group.update()
        
        #print(pg.sprite.spritecollide(self.ball, self.block_group, dokill=True))

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()
            self.input(pg.event.get())
            self.update(dt)
            self.draw()
            

if __name__ == '__main__':
    game = Game()
    game.run()
