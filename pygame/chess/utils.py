import os
import pygame as pg
from const import LETTER_COLOR

def get_scaled_image(path, res):
    cwd = os.path.dirname(os.path.abspath(__file__))
    img = pg.image.load(os.path.join(cwd, path))
    return pg.transform.smoothscale(img, res) 


def render_letter(font, letter, surface, pos):
    letter_surface = font.render(str(letter), True, LETTER_COLOR)
    letter_rect = letter_surface.get_rect(center=pos)
    surface.blit(letter_surface, letter_rect)