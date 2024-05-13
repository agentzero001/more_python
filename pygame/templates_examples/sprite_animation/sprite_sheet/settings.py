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
    
    
def get_img_frames(sheet, width, height, frame_amount, line, scalex=1, scaley=1):   
    sheet_ = get_scaled_image(sheet, (frame_amount * width, frame_amount * height))
    frames = []
    for frame in range(1, frame_amount + 1):
        image = pg.Surface((width, height))
        image.blit(sheet_, (0, 0), (width*(frame-1), height*(line-1), width*frame, height*line))
        image = pg.transform.smoothscale(image, (width*scalex, height*scaley))
        image.set_colorkey((0, 0, 0))
        frames.append(image)        
    return frames
    
    
