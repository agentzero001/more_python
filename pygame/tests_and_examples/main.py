import pygame as pg
import sys, os


class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode([W_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.image = self.get_scaled_image(path='src/img1.jpg', res = (200,200))
        
        
    @staticmethod
    def get_scaled_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)
        
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                print(event)
                
    def draw(self):
        self.screen.blit(self.image, (100, 0))
    
    def run(self):
        while True:
            self.input(pg.event.get())
            self.draw()
            pg.display.update()
    
    
    
if __name__ == '__main__':
    game = Game()
    game.run()