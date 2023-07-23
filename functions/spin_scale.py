import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.3'

#Bresenham algorithm
def line__(arr, x1, y1, x2, y2): 
    dx = abs(x2 - x1)
    sx = 1 if x1 < x2 else -1
    dy = -abs(y2 - y1)
    sy = 1 if y1 < y2 else -1
    err = dx + dy
    while True:
        arr[y1, x1] = 255
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if (e2 > dy):
            err += dy
            x1 += sx
        if (e2 < dx):
            err += dx
            y1 += sy

def rectangle(arr, a, b, c):
    d = (c[0] + a[0] - b[0], c[1] + a[1] - b[1])
    line__(arr, *a, *b)
    line__(arr, *b, *c)
    line__(arr, *c, *d)
    line__(arr, *d, *a)
    
originRotM = lambda angle: np.array([[np.cos(angle), -np.sin(angle), 0],
                                     [np.sin(angle),  np.cos(angle), 0],
                                     [0, 0, 1]])

originscaleM = lambda scaleX, scaleY: np.array([[scaleX, 0, 0],
                                                [0, scaleY, 0],
                                                [0, 0, 1]])

translationM = lambda vx, vy: np.array([[1, 0, vx],
                                        [0, 1, vy],
                                        [0, 0, 1]])



rotateM = lambda cX, cY, angle: ((translationM(cX, cY) @ originRotM(angle)) @ translationM(-cX, -cY))

scaleM = lambda cX,cY, scaleX, scaleY: ((translationM(cX, cY) @ originscaleM(scaleX, scaleY)) @ translationM(-cX, -cY))

transformation = lambda M: lambda vec: np.round(M @ [*vec, 1]).astype('int')[:2]