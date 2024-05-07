import spin_scale as m1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.2'

f = lambda scalex, scaley: m1.transformation(m1.scaleM(250, 250, scalex, scaley))
f2 = lambda mx, my: m1.transformation(m1.translationM(mx, my))
f3 = lambda angle: m1.transformation(m1.rotateM(200,200, angle)) 
f4 = lambda angle: m1.transformation(m1.rotateM(250, 250, angle))

C = np.full((500,500), 0, 'int')
rect = [(40,40), (260,40), (260, 260)]

#m1.rectangle(C, *rect)

# plt.matshow(C, origin='lower', cmap='gray')
# plt.show()


def recImg(mx, my, angle, scalex = .5, scaley = .5):
    C = np.full((500,500), 0, 'int')
    #m1.rectangle(C, *list(map(f(scale, scale), rect)))
    #m1.rectangle(C, *list(map(f2(mx,my), rect)))
    #m1.rectangle(C, *list(map(f3(angle), rect)))
    m1.rectangle(C, *list(map(f(scalex, scaley), map(f4(angle), rect))))
    #m1.hexagon(C, *list(map(f3(np.pi/2), map(f2(mx,my), hex))))    
    return C.copy()




steps = 100
images = [recImg(i,20,np.pi *i /steps) for i in range(steps)]


from PIL import Image

image_sequence = []

for frame in images:
    image = Image.fromarray(frame)  
    image_sequence.append(image)

image_sequence[0].save('animation3.gif', save_all=True, append_images=image_sequence[1:], duration=20, loop=0)