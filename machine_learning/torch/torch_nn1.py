import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.nn import functional as F

plt.rcParams['figure.facecolor'] = '.0'
plt.rcParams['axes.facecolor'] = '.1'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['xtick.color'] = 'green'
plt.rcParams['ytick.color'] = 'green'
plt.rcParams['axes.edgecolor'] = 'purple'

#hyperparameters
obs = 50
ins = 5
outs = 1
lr = .003

params = []
def weights(ins,outs):
    ws = torch.randn(ins,outs).requires_grad_(True)
    params.append(ws)
    return ws

data = np.random.choice(torch.linspace(-30,30,1000), (obs, 1))
data_unique = np.unique(data, axis=0)
obs = data_unique.shape[0]
ys = data_unique**2
ys = torch.tensor(ys).float()
xs = np.c_[torch.ones(obs), data_unique]
xs = torch.tensor(xs).float()

class Model:
    def __init__(self):
        self.w0 = weights(xs.shape[1], 100)
        self.w1 = weights(100, 50) 
        self.w2 = weights(50, ys.shape[1])
        
    def forward(self, x):
        x = torch.sin(x @ self.w0)
        x = torch.sin(x @ self.w1)
        yh = (x @ self.w2)
        return yh
        
model = Model()
optimizer = torch.optim.Adam(params, lr)

err = []
for i in range(10000):
    
    yh = model.forward(xs)  
    
    loss = F.mse_loss(yh, ys)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    e  = loss.item()
    if i % 1000 == 0:
        print('iteration {}: loss {}'.format(i, e))  
    err.append(e)
    

#show the optimization curve
plt.figure()

plt.subplot(121)
plt.plot(err,color='red', linewidth=1)
plt.title('yhat - ys')

plt.subplot(122)
plt.plot(ys, linewidth=8, label='ys', color='blue')
plt.plot(yh.detach().numpy(), linewidth=3, label='yh', color='green')
legend = plt.legend()
legend.get_texts()[0].set_color('white') 
legend.get_texts()[1].set_color('white')
plt.show()