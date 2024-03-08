import torch
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch import nn, optim, Tensor as t
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
 

class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, 200)
        self.fc2 = nn.Linear(200, num_classes)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

input_size = 784
num_classes = 10
learning_rate = .001
batch_size = 64
num_epochs = 1

mnist_path = './data'
train_dataset = datasets.MNIST(root=mnist_path, train=True, download=True,
                               transform=transforms.ToTensor())

test_dataset = datasets.MNIST(root=mnist_path, train=False, download=True, 
                              transform=transforms.ToTensor())

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader =  DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)


model = NN(input_size, num_classes).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(train_loader):
        data = data.to(device=device)
        targets = targets.to(device=device)
        
        data = data.reshape(data.shape[0], -1)
        
        scores = model(data)
        loss = criterion(scores, targets)
    
        optimizer.zero_grad()
        loss.backward()
        
        optimizer.step()
        
        
def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()
    
    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)
            x = x.reshape(x.shape[0], -1)
            
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
            
    return num_samples, num_correct
            
            