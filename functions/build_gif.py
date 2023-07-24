import spin_scale as m1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.2'


C = np.full((500,500), 0, 'int')
rect = [(40,40), (260,40), (260, 260)]
rect2 = [(30,30), (220,30), (220, 220)]


def recImg(angle, scalex, scaley, scx2 = .1, scy2 = .1):
    C = np.full((500,500), 0, 'int')
    
    m1.rectangle(C, *list(map(m1.transformation(m1.scaleM(150, 150, scalex, scaley)), 
                            map(m1.transformation(m1.rotateM(150, 150, angle)),
                                rect))))
    
    
    m1.rectangle(C, *list(map(m1.transformation(m1.scaleM(150, 150, scalex, scaley)), 
                            map(m1.transformation(m1.rotateM(150, 150, angle+1)),
                                rect))))
    
    m1.rectangle(C, *list(map(m1.transformation(m1.scaleM(150, 150, scalex, scaley)), 
                            map(m1.transformation(m1.rotateM(150, 150, angle+.5)),
                                rect))))
    
    m1.rectangle(C, *list(map(m1.transformation(m1.scaleM(200, 200, scx2, scy2)), 
                            map(m1.transformation(m1.rotateM(200, 200, angle)),
                                rect))))
    

    
    return C.copy()

steps = 200
images = [recImg(4*np.pi * i/steps, .4*i/steps, .8*i/steps, i /150) for i in range(steps)]
images += [recImg(4*np.pi * i/steps, .4, .8, i /150) for i in range(steps)]

images += list(reversed(images[:200]))

from PIL import Image

image_sequence = []

for frame in images:
    image = Image.fromarray(frame)  
    image_sequence.append(image)

image_sequence[0].save('animation2.gif', save_all=True, append_images=image_sequence[1:], duration=50, loop=0)




# m1.rectangle(C, *rect)

# L4 = np.full((100,100), 0, 'int')
# rect = [(20,20), (80,20), (80,80)]
# m1.rectangle(L4, *rect)
# m1.rectangle(L4, *list(map(m1.transformation(m1.scaleM(50, 50, 1.5, 1)), rect)))
#plt.matshow(images[20], cmap='gray', origin='lower')
