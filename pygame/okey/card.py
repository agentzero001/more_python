import pygame as pg

        
class Card(pg.sprite.Sprite):
    def __init__(self, col, xy, number):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = xy
        font = pg.font.Font(None, 36)  
        self.text = font.render(str(number), True, (0, 0, 0)) 
        self.text_rect = self.text.get_rect(center=xy)  
                
        
    def update(self):
        pass
        