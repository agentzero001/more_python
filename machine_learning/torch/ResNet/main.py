import torch
from torch import Tensor as T
from torchvision import models
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt


resnet = models.resnet101(pretrained=True)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
        )
])
breakpoint()
tiger = Image.open('unbenannt.jpg')
tiger_proc = preprocess(tiger)

batch_t = torch.unsqueeze(tiger_proc, 0)

with open('imagenet-classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]
    


resnet.eval()
out = resnet(batch_t)
out.sort(descending=True) 

_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0]
labels[index[0]], percentage[index[0]] 

_, indices = torch.sort(out, descending=True)
output = [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]] 
print(output)

