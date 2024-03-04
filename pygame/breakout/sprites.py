import pygame as pg
# from pygame.sprite import Group
from settings import *
import random


class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image  = pg.Surface((WIDTH // 10, HEIGHT // 20))        
        self.rect   = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
        self.direct = pg.math.Vector2()
        self.pos    = pg.math.Vector2(self.rect.topleft)
        self.speed  = 300
        self.image.fill('black')

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direct.x = 1
        elif keys[pg.K_LEFT]:
            self.direct.x = -1
        else:
            self.direct.x = 0

    def screen_collide(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.pos.x = self.rect.x
        if self.rect.x < 0:
            self.rect.left = 0
            self.pos.x = self.rect.x

    def update(self, dt):
        self.control()
        self.pos.x += self.direct.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screen_collide()


class Ball(pg.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)

        self.player = player
        self.image  = pg.image.load('src/graphics/other/ball.png')
        self.rect   = self.image.get_rect(midbottom=player.rect.midtop)
        self.pos    = pg.math.Vector2(self.rect.topleft)
        self.direct = pg.math.Vector2((random.choice((1, -1)), -1))
        self.speed  = 400
        self.active = False
        
    def update(self, dt):
        if self.active:
            pass
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pg.math.Vector2(self.rect.topleft)
