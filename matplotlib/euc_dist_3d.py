import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = '0.3'


A1 = np.array([5,5,5])

radius = 6
n = 500
theta = np.random.uniform(0, np.pi, n)
phi = np.random.uniform(0, 2*np.pi, n)

x = A1[0] + radius * np.sin(theta) * np.cos(phi)
y = A1[1] + radius * np.sin(theta) * np.sin(phi)
z = A1[2] + radius * np.cos(theta)

points_ = np.array([x, y, z]).T
points_ += np.random.normal(loc=0, scale=2, size=(n, points_.shape[1]))


fig = plt.figure()
fig.patch.set_facecolor('0.2')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('0.2')

ax.scatter(A1[0], A1[1], A1[2], c='black', marker='o',s=300)
ax.scatter(points_[:, 0], points_[:, 1], points_[:, 2], c='r', marker='o')

for i in range(points_.shape[0]):
    plt.plot((A1[0], points_[i, 0]), (A1[1], points_[i, 1]), (A1[2], points_[i, 2]),c='green',linewidth=.5, zorder=2)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim(-5, 15)
ax.set_ylim(-5, 15)
ax.set_zlim(-5, 15)

#plt.show()
