import pygame as pg
from pygame.math import Vector2 as vec

FPS         = 60
FIELD_COLOR = (30, 30, 30)
BG_COLOR    = (22, 70, 110)

ANIM_TIME_INTERV   = 180
FAST_ANIM_TIME_INT = 1

TILE_SIZE  = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES  = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H


INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0) 
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * .45)
MOVE_DIRECTIONS = {'left': (-1, 0), 'right' : (1, 0), 'down' : (0, 1)}

TETROMINOES = {
    'T' : [[(0, 0), (-1, 0), (1, 0), (0, -1)], (128, 128, 128)],
    'O' : [[(0, 0), (0, -1), (1, 0), (1, -1)], (150, 0, 150)],
    'J' : [[(0, 0), (-1, 0), (0, -1), (0,-2)], (128, 0, 128)],
    'L' : [[(0, 0), (1, 0), (0, -1), (0, -2)], (150, 165, 0)],
    'I' : [[(0, 0), (0, 1), (0, -1), (0, -2)], (165, 42, 42)],
    'S' : [[(0, 0), (1, 0), (0, -1), (-1, -1)], (64, 64, 64)],
    'Z' : [[(0, 0), (1, 0), (0, -1), (1, 1)], (150, 0, 0)]
}
