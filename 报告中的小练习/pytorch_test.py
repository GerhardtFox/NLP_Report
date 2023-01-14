import torch
from torch import nn

embedding = nn.Embedding(20,5,padding_idx=3)
print(embedding(torch.LongTensor([0,1,2,3,4])))
optimizer = torch.optim.SGD(embedding.parameters(),lr=0.1)
criteria = nn.MSELoss()

for i in range(1000): 
    outputs = embedding(torch.LongTensor([0,1,2,3,4]))
    loss = criteria(outputs, torch.ones(5,5))
    loss.backward()
    optimizer.step()
    optimizer.zero_grad

print(embedding(torch.LongTensor([0,1,2,3,4])))
