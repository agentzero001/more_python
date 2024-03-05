import pygame as pg
from pygame.math import Vector2 as vec

FPS = 60
FIELD_COLOR = (30, 30, 30)

ANIM_TIME_INTERVAL = 150

TILE_SIZE = 40
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0) 
MOVE_DIRECTIONS = {'left': (-1, 0), 'right' : (1, 0), 'down' : (0, 1)}

TETROMINOES = {
    'T' : [[(0, 0), (-1, 0), (1, 0), (0, -1)], (128, 128, 128)],
    'O' : [[(0, 0), (0, -1), (1, 0), (1, -1)], (255, 0, 255)],
    'J' : [[(0, 0), (-1, 0), (0, -1), (0,-2)], (128, 0, 128)],
    'L' : [[(0, 0), (1, 0), (0, -1), (0, -2)], (255, 165, 0)],
    'I' : [[(0, 0), (0, 1), (0, -1), (0, -2)], (165, 42, 42)],
    'S' : [[(0, 0), (1, 0), (0, -1), (-1, -1)], (64, 64, 64)],
    'Z' : [[(0, 0), (1, 0), (0, -1), (1, 1)], (255, 0, 0)]
}
