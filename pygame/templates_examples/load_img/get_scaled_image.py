import pygame as pg
import sys, os

class Game:
    def __init__(self, W_SIZE=600):
        pg.init()
        self.screen = pg.display.set_mode((W_SIZE,) * 2)
        self.clock = pg.time.Clock()
        self.bg = self.get_scaled_image(path='src\img1.jpg', res = (W_SIZE,) * 2)
        
    @staticmethod
    def get_scaled_image(path, res):
        cwd = os.path.dirname(os.path.abspath(__file__))
        img = pg.image.load(os.path.join(cwd, path))
        return pg.transform.smoothscale(img, res)
    
    def input(self, events):    
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            else:
                print(event)
                
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
    
    def run(self):
        while True:
            self.input(pg.event.get())
            self.draw()
            pg.display.update()    
    
if __name__ == '__main__':
    game = Game()
    game.run()