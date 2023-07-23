import spin_scale as m1
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.3'



C = np.full((300,300), 0, 'int')
rect = [(40,40), (260,40), (260, 260)]

m1.rectangle(C, *rect)

plt.matshow(C)
#m1.line__(C, )
