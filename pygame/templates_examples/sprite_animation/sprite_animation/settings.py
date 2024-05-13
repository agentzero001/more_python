import pygame as pg
import os

FPS = 60
RES = WIDTH, HEIGHT = 1280, 720
FIELD_COLOR = (20, 20, 20)
ANIM_TIME_INTERVAL = 1000
TIMER_EVENT = pg.USEREVENT + 0


def get_scaled_image(path, res):
        cwd = os.path.dirname(os.path.abspath(__file__))
        img = pg.image.load(os.path.join(cwd, path))
        return pg.transform.smoothscale(img, res) 
    
    
def get_anim_frames(name, amount, res):
    frames = [get_scaled_image('{}{}.png'.format(name, i), res) for i in range(1, amount + 1)]
    images = []
    for frame in frames:    
        image = pg.Surface(res)
        image.blit(frame, (0, 0), (0, 0, res[0], res[1]))
        image.set_colorkey((0, 0, 0))
        images.append(image)    
    return images
    
    
