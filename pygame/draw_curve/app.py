import pygame as pg
from const import *
from utils import *
from objects import Curve, Vector
import numpy as np
from numpy import sin, cos
import sys

class Render_Curve:
    def __init__(self, x_t, y_t):
        pg.init()
        self.x_t = x_t
        self.y_t = y_t
        self.str_func = x_t + ", " +  y_t
        self.f = lambda t: eval(x_t + ", " +  y_t)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.running = True
        self.curve = Curve(self, self.f)
        self.k = 0
        
        
                
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False         
                
    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        self.close()
        
    def draw(self):
        self.screen.fill((20, 20, 20))
        self.render_mouse_pos()
        self.draw_coord_system()
        self.display_function()
        self.display_current_value()
        self.curve.draw(self.k)
        self.display_velocity_vector()
        pg.display.flip()
    
    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        self.k += STEP
        self.k %= 2 * np.pi
        self.curve.update(self.k)
        
    def close(self):
        pg.quit()
        sys.exit()
        
    def draw_coord_system(self):
        pg.draw.line(self.screen, (100,100,100), conv_coords(-SIZE, 0), conv_coords(SIZE, 0), 1)
        pg.draw.line(self.screen, (100,100,100), conv_coords(0, -SIZE), conv_coords(0, SIZE), 1)    
   
    def render_mouse_pos(self):
        m_x, m_y  = pg.mouse.get_pos() 
        m_x, m_y = m_x - WIDTH // 2, - (m_y - HEIGHT // 2 )
        display_text(self.screen, "Mouse Position: ({}, {}) (not normalized)".format(m_x, m_y), (10, 10), FONT_SIZE)
        
    def display_function(self):
        display_text(self.screen, "x(t) = " + self.x_t, (10, 50), FONT_SIZE)
        display_text(self.screen, "y(t) = " + self.y_t, (10, 70), FONT_SIZE)
        
        
    def display_velocity_vector(self):
        display_text(self.screen, "x'({}) = {}".format(round(self.k, 1), self.curve.dx_dt), (10, 210), FONT_SIZE)
        display_text(self.screen, "y'({}) = {}".format(round(self.k, 1), self.curve.dy_dt), (10, 230), FONT_SIZE)
        
    def display_current_value(self):
        n_digits = 1
        k = round(self.k, n_digits)
        x, y = self.curve.current_value
        x, y = round(x, n_digits), round(y, n_digits)        
        strings = ["t = {}".format(k), "x({}) = {}".format(k, x), "y({}) = {}".format(k, y)]
        coordinates = [(10, 130), (10, 150),(10, 170)]
        for text, coords in zip(strings, coordinates):
            display_text(self.screen, text, coords, FONT_SIZE)                        
                        
                        
if __name__ == '__main__':
    app = Render_Curve(x_t = "2*sin(2*t)", y_t="1.5*cos(t)")
    #app = Render_Curve(x_t = "cos(t)", y_t="sin(t)")
    
    app.run()
    