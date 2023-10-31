import turtle as t
import colorsys
from PIL import Image

t.speed(1000)

t.bgcolor('black')
h=0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        t.color(c)
        h += 0.005
        t.rt(90)
        t.circle(150 -  j * 6, 90)
        t.lt(90)
        t.circle(150 -  j * 6, 90)
        t.rt(180)
    t.circle(40,24)
t.done()    
