import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import *


class GraphicsEngine:
    def __init__(self, win_size=(800, 600)):
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)    
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)    
        self.ctx    = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.clock  = pg.time.Clock()
        self.time   = 0
        self.delta_time = 0
        self.camera = Camera(self)
        self.scene  = Cube(self)        
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.scene.destroy()
                pg.quit() 
                sys.exit()    
    
    def render(self):
        self.ctx.clear(color=(.08, .16, .18))
        self.scene.render()
        pg.display.flip()
        
    def get_time(self):
        self.time = pg.time.get_ticks() * .001
        
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)
    
if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()