import pygame as pg
import numpy as np
from utils import conv_coords
from const import *
import sympy as sp



class Curve:   
    def __init__(self, app, f):
        self.t = 0
        self.f = f
        self.app = app
        self.current_value = (0, 0)

    def draw_line(self, k, n=200):
        a, b = k - .5, k
        t = np.linspace(a, b, n)
        values = [conv_coords(x, y) for x, y in zip(*self.f(t))]
        pg.draw.aalines(self.app.screen, GREY, False, values, 1) 
        
        
    def draw_point(self, t):
        x, y = self.f(t)
        pg.draw.circle(self.app.screen, (200, 0, 0), conv_coords(x, y), 5)
        return x, y
        
    def draw(self, k):
        self.draw_line(k)
        self.current_value = self.draw_point(k)
    
    def update(self):
        pass
    
    
    