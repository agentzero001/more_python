import sys
import pygame as pg
from settings import *
from player import *
import map_


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        self.count = 0
        self.toggle_overlay = False

    def overlay(self):
        text_color = (0, 0, 0)
        overlay_surface = pg.Surface((RES), pg.SRCALPHA)
        pg.draw.rect(overlay_surface, (100, 100, 100, 200), (10, 10, 300, 500))
        font = pg.font.SysFont(None, 30)
        text_variables = [
        ("map_pos", self.player.map_pos), 
        ("pos", (round(self.player.pos[0], 2), round(self.player.pos[1], 2))),
        ("dx, dy", (round(self.dx, 4), round(self.dy, 4))),
        ("pos", (round(self.player.pos[0]*100, 2), round(self.player.pos[1]*100, 2)))
        ]
        
        y_position = 20
        for tuple_ in text_variables:
            text = "{}: {}".format(*tuple_)
            text_surface = font.render(text, True, text_color)
            overlay_surface.blit(text_surface, (15, y_position))
            y_position += 20 
        self.screen.blit(overlay_surface, (0, 0))

    def new_game(self):
        self.map1 = map_.Map(self)
        self.player = Player(self)

    def update(self):
        self.dx, self.dy = self.player.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map1.draw()
        self.player.draw()
        if self.toggle_overlay:
                self.overlay()
        

    def check_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if (event.type == pg.QUIT
                    or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:
                self.anim_trigger = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_o:
                    self.toggle_overlay = not self.toggle_overlay
                                

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = Game()
    app.run()
