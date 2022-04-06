import torch
from torch import nn


class imageNet(nn.Module):
    def __init__(self, output_length):
        super().__init__()
        self.model = nn.Sequential(
                        nn.Linear(1, 64),
                        nn.ReLU(),
                        nn.Linear(64, 16*16),
                        nn.ReLU(),
                        nn.Linear(16*16, output_length),
                        nn.Sigmoid()
                        )

    def forward(self, x):
        x = torch.from_numpy(x).float()
        return self.model(x)*255
        
