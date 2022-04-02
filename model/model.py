import torch
from torch import nn


class imageNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
                        nn.Linear(1, 64),
                        nn.ReLU(),
                        nn.Linear(64, 16*16),
                        nn.ReLU(),
                        nn.Linear(16*16, 3*64*64)
                        )

    def forward(self, x):
        return self.model(x)
        
