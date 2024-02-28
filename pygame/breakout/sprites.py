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
        
        
        
    def control(self, pressed_k):
        if pressed_k == pg.K_LEFT:
            self.direction = MOVE_DIRECTIONS['left']
        elif pressed_k == pg.K_RIGHT:
            self.direction = MOVE_DIRECTIONS['right']
            
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        
    def update(self):
        pass