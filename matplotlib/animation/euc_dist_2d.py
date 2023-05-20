import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.rcParams['figure.facecolor'] = '0.3'



A = np.array([5, 5])
t = np.linspace(0, 4*np.pi-4*np.pi/200, 200)
points = np.zeros((200, 2))
points[:, 0] = A[0] + 5 * np.cos(t)
points[:, 1] = A[1] + 5 * np.sin(t)
points += np.random.randn(200,2)*.5
distances = np.linalg.norm(points - A, axis=1)



fig = plt.figure()
plt.gca().set_facecolor('0.0')
scatter_yellow = plt.scatter(A[0], A[1], c='y', marker='o', zorder=3, s=90)
scatter_red = plt.scatter(points[:, 0], points[:, 1], c='red', marker='o', zorder=3, s=10)
lines = []
for i in range(len(points)):
    line, = plt.plot([A[0], points[i, 0]], [A[1], points[i, 1]], c='green', linewidth=.2, zorder=2)
    lines.append(line)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 12)
plt.ylim(-2, 12)
plt.grid(alpha=0.3,zorder=1)


def update(frame):
    progress = frame / 100
    new_points = (1 - progress) * A + progress * points
    scatter_red.set_offsets(new_points)
    for i, line in enumerate(lines):
        line.set_data([new_points[i, 0], A[0]], [new_points[i, 1], A[1]])
        
anim = FuncAnimation(fig, update, frames=100, interval=50, repeat=True)
plt.show()



anim.save('animation.gif', writer='pillow')