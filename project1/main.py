import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.facecolor'] = '0.3'


A = np.array([2, 7])
B = np.array([8, 6])

distance = round(np.linalg.norm(B - A), 4)
distance2 = np.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)


plt.figure()
plt.gca().set_facecolor('0.1')

plt.plot([A[0], B[0]], [A[1], B[1]], c='green', zorder=2, label='distance = {}'.format(distance))
plt.scatter(A[0], A[1], c='r', marker='o', zorder=3, label='A = ({}, {})'.format(A[0], A[1]))
plt.scatter(B[0], B[1], c='yellow', marker='o', zorder=3, label='B = ({}, {})'.format(B[0], B[1]))

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc='upper right')
plt.legend().get_frame().set_alpha(0.3)
plt.grid(alpha=0.3,zorder=1)
plt.show()