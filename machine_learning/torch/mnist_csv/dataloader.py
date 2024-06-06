import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math

class CustomDataset(Dataset):
    def __init__(self, root, filename, transform=None):
        self.filename = filename
        self.root = root
        xy = np.loadtxt('{}/{}'.format(root, filename), delimiter=',', dtype=np.float32, skiprows=1)
        self.x = torch.from_numpy(xy[:, 1:])
        self.y = torch.from_numpy(xy[:, 0])
        self.n_samples = xy.shape[0]
        self.transform = transform
        
    def __repr__(self):
        transform_repr = repr(self.transform) if self.transform else 'None'
        return (f"Dataset {self.__class__.__name__}\n"
                f"    Number of datapoints: {self.n_samples}\n"
                f"    Root location: {self.root}\n"
                f"    Filename: {self.filename}\n"
                f"    Transform: {transform_repr}")
        
    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.n_samples   