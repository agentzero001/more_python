import pygame as pg
from settings import *
from sprite import Entity
from player import Player



class Scene:
    def __init__(self, app):
        self.app = app
        self.sprites = pg.sprite.Group()
        self.entity = Entity([self.sprites])
        Entity([self.sprites], pos=(100, 100))
        self.player = Player([self.sprites])
    
    def update(self):
        self.sprites.update()
    
    def draw(self):
        self.app.screen.fill('black')
        self.sprites.draw(self.app.screen)
        
        
