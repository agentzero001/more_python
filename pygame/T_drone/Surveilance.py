from djitellopy import tello
import module1 as m1
import cv2
import time
import pygame as pg





m1.d1.connect()
m1.d1.streamon()
print(m1.d1.get_battery())


while True:
    
    frame = m1.d1.get_frame_read().frame
    frame = cv2.resize(frame, m1.w_size)
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    frame = cv2.flip(frame, 0)


    surface = pg.surfarray.make_surface(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    m1.screen.blit(surface, (0, 0))
    pg.display.flip()


    # cv2.imshow('camera1', frame)
    # cv2.waitKey(1)
    
    
    values = m1.set_control(frame)
    m1.d1.send_rc_control(values[0], values[1], values[2], values[3])
    
    
    # if m1.getKey('p'):
    #     a+=1
    #     cv2.imwrite('Resources/Images/{}.jpg'.format(a), frame)
    #     time.sleep(.2)  
