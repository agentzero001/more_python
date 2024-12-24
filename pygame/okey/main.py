import sys 
import pygame as pg
from card import Card
from settings import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('App')
        self.screen  = pg.display.set_mode(WIN_SIZE)
        self.clock   = pg.time.Clock()
        #self.obj     = Object(self.sprites)
        self.cards = [Card(*data) for data in CARD_DATA]
        self.sprite_cards = pg.sprite.Group(self.cards) 

    def update(self):
        self.clock.tick(FPS) 
        self.draw()
        #self.square.update()  #the sprites.update is alrdy calling the Square update method
        self.sprite_cards.update()
        
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.sprite_cards.draw(self.screen)
        for card in self.sprite_cards:
            self.screen.blit(card.text, card.text_rect)
        

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT 
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                
                for card in self.sprite_cards:
                    if card.rect.collidepoint(pos):
                        card.image.fill((20, 20, 20))
                # for cards in self.cards:
                #     if pos.
                
    def run(self):
        while True:
            #print(self.sprites)
            self.check_events()
            self.update()
            pg.display.flip()            

        
           
if __name__ == '__main__':
    app = App()
    app.run()
    