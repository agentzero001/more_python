import spin_scale as m1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.2'


C = np.full((100,100), 0, 'int')
rect = [(20, 15), (30, 15), (30, 40)]
m1.rectangle(C, *rect)

# plt.matshow(C, origin='lower', cmap='gray')
# plt.show()


f = lambda scalex, scaley: m1.transformation(m1.scaleM(30, 30, scalex, scaley))
f2 = lambda mx, my: m1.transformation(m1.translationM(mx, my))

def recImg(mx, my):
    C = np.full((100,100), 0, 'int')
    #m1.rectangle(C, *list(map(f(scale, scale), rect)))
    m1.rectangle(C, *list(map(f2(mx,my), rect)))    
    return C.copy()




# def recImg(angle, scale):
#     C = np.full((60,60), 0, 'int')
#     m1.rectangle(C, *list(map(m1.transformation(m1.scaleM(30, 30, scale, scale)), 
#                             map(m1.transformation(m1.rotateM(30, 30, angle)),
#                                 rect))))
#     return C.copy()

steps = 100
images = [recImg(i, i) for i in range(steps)]


for i in range(steps):
    images.append()



from PIL import Image

image_sequence = []

for frame in images:
    image = Image.fromarray(frame)  
    image_sequence.append(image)

image_sequence[0].save('animation3.gif', save_all=True, append_images=image_sequence[1:], duration=20, loop=0)