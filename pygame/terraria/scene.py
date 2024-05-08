import pygame as pg
from settings import *
from main import Game
from sprite import Entity



class Scene:
    def __init__(self, app: Game):
        self.app = app
        self.sprites = pg.sprite.Group()
        self.entity = Entity()
        
        
    def update(self):
        pass
    
    def draw(self):
        self.app.screen.fill('black')
