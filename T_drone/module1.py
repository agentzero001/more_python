import pygame as pg
from djitellopy import tello
import time
import cv2



global img
d1 = tello.Tello()


            
pg.init()
pg.display.set_mode((200, 200))

            
def getKey(kname):
    pressed = False
    for eve in pg.event.get(): pass
    keyInput = pg.key.get_pressed()
    myKey = getattr(pg, 'K_{}'.format(kname))
    if keyInput[myKey]:
       pressed = True
    pg.display.update()
    return pressed

def set_control():
    a = 0
    ticks = 10
    up_down, left_right, fwards_bwards, turn = 0, 0, 0, 0
    
    if   getKey('UP'):   up_down =  ticks
    elif getKey('DOWN'): up_down = -ticks
    
    if   getKey('LEFT'):  turn =  ticks
    elif getKey('RIGHT'): turn = -ticks
         
    if   getKey('w'): fwards_bwards =  ticks
    elif getKey('s'): fwards_bwards = -ticks
         
    if   getKey('a'): left_right =  ticks
    elif getKey('d'): left_right = -ticks
    
    if   getKey('c'): d1.land()
    elif getKey('v'): d1.takeoff()
    
    if getKey('p'):
        cv2.imwrite('Resources/Unages/picture{}'.format(time.time()),img)
        time.sleep(.2)  

        
           
    return [left_right, fwards_bwards, up_down, turn]    
    
    




# while True:
#     if getKey('a'):
#         print('a pressed')
        
#     if getKey('b'):
#         print('b pressed')
        
#     if getKey('s'):
#         print('s pressed')
        
#     if getKey('d'):
#         print('d pressed')


# def key_controller():
#     a=0
#     pg.init()
#     pg.display.set_mode((200, 200))
#     while True:
#         for event in pg.event.get():
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_w:
#                     print('w pressed')
#                 elif event.key == pg.K_k:
#                     print('k pressed')
#         keys = pg.key.get_pressed()
#         if keys[pg.K_a]:
#             a+=1
#             print(a)


if __name__ == '__main__':
    pass
