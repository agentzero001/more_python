import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams['figure.facecolor'] = '0.3'


_2d_TM = lambda a,b,c,d: np.array([[a,b],
                                   [c,d]])

def _2d_lin_trans(M,xylim=50):
    
    x = np.arange(-40, 41, 4)
    y = np.arange(-40, 41, 4)
    X, Y = np.meshgrid(x, y)
    coordinates = np.column_stack((X.ravel(), Y.ravel()))
    v = coordinates.T    
    v_t = M @ v
    #determinant = a*d - b*c
    print(M[0,0] * M[1,1] - M[0,1] * M[1,0])
    fig = plt.figure(figsize=(6,6))
    plt.rcParams['figure.facecolor'] = '.1'
    plt.axes().set_facecolor('black')
    scatter = plt.scatter(v[0, :], v[1, :], c='red', zorder=2, s=30, alpha=.2)
    scatter_t = plt.scatter(v_t[0, :], v_t[1, :], c='orange', zorder=2, alpha=.5)
    lines = []
    for i in range(v.shape[1]):
        line, = plt.plot([v[0, i], v_t[0, i]], [v[1, i], v_t[1, i]], c='green', linewidth=.5, zorder=1)
        lines.append(line)
    
    
    plt.axis('equal')
    plt.axhline(y=0, color='black',zorder=0)
    plt.axvline(x=0, color='black',zorder=0)
    plt.xlim(-xylim, xylim)
    plt.ylim(-xylim, xylim)
    plt.grid(alpha=.2)
    
    

    def update(frame):
            progress = frame / 200
            new_v_t = (1 - progress) * v + progress * v_t
            scatter_t.set_offsets(new_v_t.T)
            for i, line in enumerate(lines):
                line.set_data([v[0, i], new_v_t[0, i]], [v[1, i], new_v_t[1, i]])

    anim = FuncAnimation(fig, update, frames=200, interval=50, repeat=True)
    anim.save('animation2.gif', writer='pillow') 
    plt.show()


TM = _2d_TM(1, 10, -2, 1)

_2d_lin_trans(TM, xylim=100)


