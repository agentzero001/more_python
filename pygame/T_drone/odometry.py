from djitellopy import tello
import module1 as m1
import numpy as np
import cv2


fSpeed = 0
aSpeed = 0
interval = .25

dInterval = fSpeed*interval
aInterval = fSpeed*interval

x, y = 500, 500

# m1.d1.connect()
# m1.d1.streamon()
# print(m1.d1.get_battery())

def draw_points():
    cv2.circle(img_, (x, y), 5, (0 ,0 , 255), cv2.FILLED)


while True:
    #values = m1.set_control()
    #m1.d1.send_rc_control(values[0], values[1], values[2], values[3])
    
    img_ = np.zeros((800,800,3), np.uint8)
    draw_points()
    cv2.imshow('matrix', img_)
    cv2.waitKey(1)