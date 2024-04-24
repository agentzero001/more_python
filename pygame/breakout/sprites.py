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
        self.image.fill('black')
        
    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direct.x = 2
        elif keys[pg.K_LEFT]:
            self.direct.x = -2
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
        self.pos.x += self.direct.x * PLAYER_SPEED * dt
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
        self.active = False
        
    def reset_ball(self):
        if self.rect.bottom > HEIGHT:
            self.active = False
            self.direct[1] = -1
    
    def window_collide(self, direction):
        if direction == 'horizontal':
            if self.rect.x < 0:
                self.direct[0] = 1
            if self.rect.right > WIDTH:
                self.direct[0] = -1
        if direction == 'vertical':
            if self.rect.top <= 0:
                self.direct[1] = 1
                
    def player_collide(self):        
        if (self.rect.bottom >= self.player.rect.top
            and self.player.rect.right > self.rect.midbottom[0] > self.player.rect.left):
            self.direct[1] = -1
        
    def update(self, dt):
        if self.active: 
            
            if self.direct.magnitude != 0:
                self.direct = self.direct.normalize()
              
            
            self.pos.x += self.direct.x * BALL_SPEED * dt
            self.rect.x = round(self.pos.x)
            self.window_collide('horizontal')
            
            self.pos.y += self.direct.y * BALL_SPEED * dt
            self.rect.y = round(self.pos.y)
            self.window_collide('vertical')
            
            self.player_collide()
            self.reset_ball() 
            
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pg.math.Vector2(self.rect.topleft)
            
            
class Blocks(pg.sprite.Sprite):
    def __init__(self, groups, ball, x, y):
        super().__init__(groups)
        
        self.ball = ball
        self.size = BLOCK_SIZE
        self.image  = pg.Surface(BLOCK_SIZE)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.image.fill(random.choice(COLORS))
        
        
    def update(self):
        pass
        
        
        
    
    # def ball_collide(self, direction):
    #     if direction == 'h':
    #         if self.
    #     if direction == 'v':
    #         pass