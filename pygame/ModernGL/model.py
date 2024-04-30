import numpy as np

class Triangle:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vertex_buff_obj()
        self.shader_program = self.get_shader_program('default')
        self.vao = self.get_vertex_array_object()
        
    def render(self):
        self.vao.render()
    
    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
        
    def get_vertex_array_object(self):
        return self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
    
    def get_vertex_data(self):
        return np.array([(-.6, -.8, 0), (.6, -.8, 0), (.0, .8, 0)], dtype='f4')
    
    def get_vertex_buff_obj(self):
        return self.ctx.buffer(self.get_vertex_data())
    
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
            
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
            
        return self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        