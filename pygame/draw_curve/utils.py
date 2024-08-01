import pygame as pg
from const import * 

conv_coords = lambda x, y: (
    (x + MAX_X) / 6 * WIDTH, 
    (MAX_Y - y) / 6 * HEIGHT
)

def display_text(screen, text, pos, size, color=GREY):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, GREY)
    screen.blit(text_surface, pos)
    
    
    