import torch
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch import nn, optim, Tensor as t
from torch.utils.data import DataLoader #easier dataset management (mini-batches, etc)
import matplotlib.pyplot as plt
import numpy as np



mnist_path = './data'

train_dataset = datasets.MNIST(root=mnist_path, train=True, download=True)

test_dataset = datasets.MNIST(root=mnist_path, train=False, download=True)

img, label = train_dataset[0]

