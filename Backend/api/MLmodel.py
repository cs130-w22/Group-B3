import torch

class MLmodel(torch.Model):
    def __init__(self):
        super().__init__(self, partialCNN)
        self.c1 = Conv2d(1, 1, (3,3), _)
        self.relu = 0

    def forward(self, x):
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
        x = ReLU(self.c1(x))
