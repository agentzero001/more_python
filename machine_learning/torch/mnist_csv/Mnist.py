
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import warnings
warnings.filterwarnings('ignore')






data_mnist = np.loadtxt('mnist_test.csv', delimiter=',')





labels = data_mnist[:, 0]
pixels = data_mnist[:, 1:]
labels[:6]





data_t = [(pixels[i], int(labels[i])) for i in range(len(labels))]
data_t[0][1]





fig, axs = plt.subplots(1, 6, figsize=(10, 5),facecolor='grey',sharey=True)

for ax, data, l in zip(axs, pixels[10:16], labels[10:16]):
    image = data.reshape(28, 28)
    ax.imshow(image, cmap='gray')
    ax.set_title(str(int(l)))
    
plt.show()



image1 = np.array(pixels[0],dtype='uint8').reshape(28,28)

plt.figure(facecolor='grey', figsize=(2,2))
plt.imshow(image1,cmap=cm.gray)





x = np.arange(0, 28, 1)
y = np.arange(0, 28, 1)
X, Y = np.meshgrid(x, y)
Z = image1[X, Y]




fig = plt.figure(facecolor='0.1',figsize=(4,4))
ax = fig.gca(projection = '3d')
ax.set_facecolor('0.1')
ax.plot_surface(X, Y, Z,cmap=cm.gray)
plt.show()





