import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.3'


#sin_ = lambda x: np.sin(x)
#cos_ = lambda x: np.cos(x)
#y_sin = sin_(x)
#y_cos = cos_(x)
#x = np.linspace(0, np.pi*4, 1000)


func = lambda x: x**2
der_func = lambda x: 2*x


x2 = np.arange(-100,100,.1)
y = func(x2)


curr_pos = (50, func(50))
l_rate = .003

for i in range(1000):    

    new_x = curr_pos[0] - l_rate * der_func(curr_pos[0])
    new_y = func(new_x)
    curr_pos= (new_x, new_y)    
    
    plt.axes().set_facecolor('black')
    plt.plot(x2, y, c='green',zorder=1)
    plt.scatter(curr_pos[0], curr_pos[1],zorder=2,color='red')
    plt.pause(.001)
    plt.clf()