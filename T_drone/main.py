from djitellopy import tello
import time
import module1

d1 = tello.Tello()
d1.connect()
print(d1.get_battery()) 

d1.takeoff()
d1.send_rc_control(0, 0, 0, 0) 
time.sleep(4)
#d1.send_rc_control(0, 0, 0, 0)
d1.land()


#module1.key_controller()

