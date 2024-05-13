import pygame as pg
from settings import *
   
class Player(pg.sprite.Sprite):
    def __init__(self, app, x, y):
        self.app = app
        self.x = x
        self.y = y
        pg.sprite.Sprite.__init__(self)
        self.img_res = [256] * 2
        self.default_image = get_scaled_image('assets/champion.png', self.img_res)
        self.image = self.default_image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.anim_trigger = 50
        self.defend_time = 1500
        self.frame = 0
        self.time = pg.time.get_ticks()
        self.attack_frames = get_anim_frames('assets/champion-attack-', 6, self.img_res)
        self.attack_trigger = False
        self.defend_trigger = False
        
        
    def update(self):
        if self.attack_trigger:
            self.attack()
            
        if self.defend_trigger:
            self.defend()
    
    def defend(self):
        curr_time = pg.time.get_ticks()
        self.image = get_scaled_image('assets/champion-defend.png', self.img_res)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        if curr_time - self.time > self.defend_time:
            self.image = self.default_image
            self.defend_trigger = False
            self.time = curr_time
        
    def attack(self):
        curr_time = pg.time.get_ticks()
        if curr_time - self.time > self.anim_trigger:
            self.switch_frame(self.frame)
            self.frame += 1 
            self.time = curr_time
            if self.frame >= len(self.attack_frames):
                self.image  = self.default_image
                self.frame = 0
                self.attack_trigger = False
        
    def switch_frame(self, fr):
        self.image = self.attack_frames[fr]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)