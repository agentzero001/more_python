import pygame as pg
from random import randrange

vec2 = pg.math.Vector2

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_pos()
        self.direction = vec2(0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {key: 1 for key in [pg.K_w, pg.K_a, pg.K_s, pg.K_d]}
        
    get_random_pos = lambda self: [randrange(self.size // 2 ,
                                             self.game.W_SIZE - self.size // 2,
                                             self.size), 
                                   randrange(self.size // 2 ,
                                             self.game.W_SIZE - self.size // 2,
                                             self.size)] 
    
    def border_collision(self):
        if self.rect.left < 0 or self.rect.right > self.game.W_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.W_SIZE:
            self.game.new_game()
            
    def self_eat(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()
    
    def control(self, event):
        if event.type == pg.KEYDOWN:
                        
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pg.K_w: 1, pg.K_s: 0, pg.K_d: 1, pg.K_a: 1}
                
            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pg.K_w: 0, pg.K_s: 1, pg.K_d: 1, pg.K_a: 1}
                    
            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)               
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 0, pg.K_a: 1}
                 
            if event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1, pg.K_a: 0}
    
    
    def reposition(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_pos()
            self.length += 1
            
    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False   
    
    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]
    
    def update(self):
        self.self_eat()
        self.reposition()
        self.border_collision()
        self.move()
    
    def draw(self):
        tuple(pg.draw.rect(self.game.screen,
                           (120,120,120),
                           segment) 
              for segment in self.segments) 
                
class Food:
    
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.game.snake.get_random_pos()
        
    def draw(self):
        pg.draw.rect(self.game.screen, (150,0,0), self.rect)
        
