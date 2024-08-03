import pygame as pg
import numpy as np
from utils import conv_coords
from const import *
import math
import sympy as sp
from pygame import Vector2 as V


class Curve:   
    def __init__(self, app, f):
        self.t = 0
        self.f = f
        self.app = app
        self.x, self.y = 0, 0
        self.current_value = (0, 0)
        self.velocity_vector = Vector(self.app, 0, 0)
        self.dx_dt, self.dy_dt = (0, 0)
    

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
        self.velocity_vector.draw()
    
    def update(self, t):
        self.update_velocity_vector(t)
        self.velocity_vector.update(*self.current_value)
    
    def update_velocity_vector(self, t):
        dt = .0001
        x, y = self.f(t)
        d_x, d_y = self.f(t + dt)
        v_x = (d_x - x) / dt
        v_y = (d_y - y) / dt
        self.velocity_vector.x = v_x
        self.velocity_vector.y = v_y
        self.dx_dt = round(v_x, 2)
        self.dy_dt = round(v_y, 2)
        
        
              
    
class Vector:
    def __init__(self, app, x, y):
        self.app = app
        self.x = x
        self.y = y
        self.start = (0, 0)
        self.end = (self.x, self.y)
        print(abs(self))
        
    def __abs__(self):
        return np.sqrt(self.x ** 2 + self.y **2)
    
    def draw(self):
        pg.draw.aaline(self.app.screen, GREY, conv_coords(*self.start), conv_coords(*self.end))      
        
    def update(self, x, y):
        self.start = x, y
        self.end = x + self.x, y + self.y
        
        