import os
import pygame as pg

def get_scaled_image(path, res):
        cwd = os.path.dirname(os.path.abspath(__file__))
        img = pg.image.load(os.path.join(cwd, path))
        return pg.transform.smoothscale(img, res) 