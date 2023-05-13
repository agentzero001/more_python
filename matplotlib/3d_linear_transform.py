import numpy as np
import matplotlib.pyplot as plt


_3d_TM = lambda x1,y1,z1,x2,y2,z2,x3,y3,z3: np.array([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])

def _3d_lin_trans(M, xyzlim=50):
    
    x = np.arange(-20, 21, 10)
    y = np.arange(-20, 21, 10)
    z = np.arange(-20, 21, 10)

    X, Y, Z = np.meshgrid(x, y, z)
    coordinates = np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))
    v = coordinates.T    
    v_t = M @ v
        
    fig = plt.figure()
    fig.patch.set_facecolor('.1')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('.1')
    ax.scatter(v[0,:], v[1,:], v[2,:], c='red',alpha=.5, s=50)
    ax.scatter(v_t[0,:], v_t[1,:], v_t[2,:], c='black',alpha=.3,s=50)
    for i in range(v.shape[1]):
        plt.plot([v[0, i], v_t[0, i]], [v[1, i], v_t[1, i]], [v[2, i], v_t[2, i]],c='g',linewidth=.5, zorder=0)
    ax.set_xlim(-xyzlim, xyzlim)
    ax.set_ylim(-xyzlim, xyzlim)
    ax.set_zlim(-xyzlim, xyzlim)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    
M1 = _3d_TM(2,0,0,0,2,0,0,0,2)

_3d_lin_trans(M1)
