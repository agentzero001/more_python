import numpy as np 
import pycuda. autoinit
from pycuda import gpuarray
from time import time

host_data = np.float32(np.random.random(5_000_000))

t1 = time()
host_data_2x = host_data * np.float32(2)
t2 = time()

print('time to compute on cpu: {}'.format(t2-t1))


device_data = gpuarray.to_gpu(host_data)

t1 = time()
device_data_2x = device_data * 2
t2 = time()

from_device = device_data_2x.get()

print('time to compute on gpu: {}'.format(t2-t1))


print(np.allclose(from_device, host_data_2x))