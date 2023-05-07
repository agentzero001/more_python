from djitellopy import tello
import time
import module1 as m1




d1 = tello.Tello()
d1.connect()
print(d1.get_battery()) 


def set_control():
    ticks = 10
    up_down, left_right, fwards_bwards, turn = 0, 0, 0, 0
    
    if   m1.getKey('UP'):   up_down =  ticks
    elif m1.getKey('DOWN'): up_down = -ticks
    
    if   m1.getKey('LEFT'):  turn =  ticks
    elif m1.getKey('RIGHT'): turn = -ticks
         
    if   m1.getKey('w'): fwards_bwards =  ticks
    elif m1.getKey('s'): fwards_bwards = -ticks
         
    if   m1.getKey('a'): left_right =  ticks
    elif m1.getKey('d'): left_right = -ticks
    
    if    m1.getKey('c'): d1.land()
    elif  m1.getKey('v'): d1.takeoff()
        
    return [up_down, fwards_bwards, left_right, turn]



 


while True:
    values = set_control()
    d1.send_rc_control(values[2], values[1], values[0], values[3])
    time.sleep(.1)
    
    