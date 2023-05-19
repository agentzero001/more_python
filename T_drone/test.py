import numpy as np


grades = np.array([[11, 8, 5, 6, 9, 12, 6, 6, 12, 9, 3, 14, 11, 14, 6, 6, 8, 12, 3, 9, 12],
                   [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1]])  

data = np.c_[grades[0,:], grades[1,:]]


X = data[:, 0]
Y = data[:, 1]


s = list(map(lambda x, y: len(X[(X == x) & (Y == y)]), X, Y))

s