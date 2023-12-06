from settings import  * 
import pygame as pg
import math


class RayCasting:
    def __init__(self, game):
        self.game = game
        
    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
            
    def update(self):
        self.raycast()
        
    