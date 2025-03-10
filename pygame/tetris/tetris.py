import pygame as pg
from settings import *
from tetromino import Tetromino
import math


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array  = self.get_field_array()
        self.tetromino    = Tetromino(self)
        self.n_tetromino  = Tetromino(self, current=False)
        self.speed_up = False
        
    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]
                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)    
            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

    def store_blocks(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block        
        
    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]
    
    def check_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True
        
    def check_tetromino_landing(self):
        if self.tetromino.landed:
            if self.check_game_over():
                self.app.new_game()
            else:
                self.speed_up = False
                self.store_blocks()
                self.n_tetromino.current = True
                self.tetromino = self.n_tetromino
                self.n_tetromino = Tetromino(self, current=False)
                 
    def control(self, pressed_k):
        if pressed_k == pg.K_LEFT:
            self.tetromino.move('left')
        elif pressed_k == pg.K_RIGHT:
            self.tetromino.move('right')
        elif pressed_k == pg.K_UP:
            self.tetromino.rotate()
        elif pressed_k == pg.K_DOWN:
            self.speed_up = True
            
    def draw_grid(self):
        for x in range(FIELD_W):
           for y in range(FIELD_H):
               pg.draw.rect(self.app.screen, 'black', 
                            (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        
    def update(self):
        trigger = [self.app.anim_trigger, self.app.anim_trigger_f][self.speed_up]
        if trigger:
            self.check_full_lines()          
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()
                    
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)    