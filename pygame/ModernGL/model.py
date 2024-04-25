import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
    
    def get_vertex_data(self):
        vertex_data = np.array([(-.6, -.8, .0), (.6, -.8, .0), (.0, .8, .0)], dtype='f4')
        return vertex_data
    
    def get_vertex_buff_obj(self):
        return self.ctx.buffer(self.get_vertex_data())