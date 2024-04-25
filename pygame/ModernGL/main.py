import pygame as pg
import moderngl as mgl
import sys

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        pg.init()
        self.WINSIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        pg.display.set_mode(self.WINSIZE, flags=pg.OPENGL | pg.DOUBLEBUF)        
        self.ctx = mgl.create_context()
        self.clock = pg.time.Clock()
          
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()    
    
    def render(self):
        self.ctx.clear(color=(.08, .16, .18))
        pg.display.flip()
        
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)
    
        
if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()