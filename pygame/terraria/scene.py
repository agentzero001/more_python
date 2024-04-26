import pygame as pg
from settings import *


class Scene:
    def __init__(self, app):
        self.app = app
        
    def update(self):
        pass
    
    def draw(self):
        self.app.screen.fill('black')
