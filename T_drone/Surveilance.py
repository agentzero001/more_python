from djitellopy import tello
import module1 as m1
import cv2
import time

m1.d1.connect()
m1.d1.streamon()
print(m1.d1.get_battery())


while True:
    img = m1.d1.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow('camera1', img)
    cv2.waitKey(1)
    
    
    values = m1.set_control()
    m1.d1.send_rc_control(values[0], values[1], values[2], values[3])
    time.sleep(.1)  
    
    
    # if m1.getKey('p'):
    #     cv2.imwrite('Resources/Unages/picture{}'.format(time.time()),img)
    #     time.sleep(.2)  
