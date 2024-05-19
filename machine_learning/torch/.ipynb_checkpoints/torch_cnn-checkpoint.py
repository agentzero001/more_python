import torch
import torch.nn.functional as F
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch import nn, optim, Tensor as t
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
 

class CNN(nn.Module):
    def __init__(self, in_channels=1, num_classes=10):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=8, kernel_size=(3,3), stride=(1,1), padding=(1,1))
        self.pool = nn.MaxPool2d(kernel_size=(2,2), stride=(2,2))
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=(3,3), stride=(1,1), padding=(1,1))
        self.fc1 = nn.Linear(16*7*7, num_classes)
                
        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
    
        return x

    
    
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

num_classes = 10
learning_rate = .001
batch_size = 64
num_epochs = 5

mnist_path = './data'
train_dataset = datasets.MNIST(root=mnist_path, train=True, download=True,
                               transform=transforms.ToTensor())

test_dataset = datasets.MNIST(root=mnist_path, train=False, download=True, 
                              transform=transforms.ToTensor())

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader =  DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)


model = CNN().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(train_loader):
        data = data.to(device=device)
        targets = targets.to(device=device)
        
        
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
            
            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
            
    return num_samples, num_correct
            
            