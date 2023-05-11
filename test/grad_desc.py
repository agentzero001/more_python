import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.facecolor'] = '0.3'
plt.axes().set_facecolor('black')



func = lambda x: x**2
der_func = lambda x: 2*x

sin_ = lambda x: np.sin(x)
cos_ = lambda x: np.cos(x)

x = np.linspace(0, np.pi/2, 1000)
x2 = np.arange(-100,100,.1)
y = func(x)
y_sin = sin_(x)
y_cos = cos_(x)



#cur_pos = (50, func(50))
l_rate = .1

# for i in range(1000):
#     new_x = cur_pos[0] - l_rate * der_func(cur_pos[0])
    
  




plt.plot(x,y_cos, c='red',zorder=1)
plt.plot(x,y_sin, c='green',zorder=1)

#plt.scatter(cur_pos[0], cur_pos[1],zorder=2)


plt.show()
