import pygame as pg
#from pygame.sprite import Group
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.image = pg.Surface((WIDTH // 10, HEIGHT // 20))
        self.image.fill('black')
        
        self.rect = self.image.get_rect(midbottom = (WIDTH // 2, HEIGHT - 20))
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.speed = 300       
        
        
    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        
    def update(self, dt):
        self.control()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)