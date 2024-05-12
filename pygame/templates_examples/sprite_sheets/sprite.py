import pygame as pg
from settings import *
   
class Player(pg.sprite.Sprite):
    def __init__(self, app, x, y, sheet_line):
        self.app = app
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)
        self.frame_amount = 10
        self.frames = get_img_frames('assets/warrior.png', 32, 32, self.frame_amount, sheet_line, 2, 2)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.anim_trigger = 100
        self.frame = 0
        self.time = pg.time.get_ticks()
        
        
    def update(self):
        self.curr_time = pg.time.get_ticks()
        if self.curr_time - self.time > self.anim_trigger:
            self.switch_frame(self.frame)
            self.frame += 1 
            self.time = self.curr_time
            if self.frame >= self.frame_amount:
                self.frame = 0
        
    def switch_frame(self, fr):
        self.image = self.frames[fr]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)