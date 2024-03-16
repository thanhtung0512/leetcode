import torch
import torch.nn as nn
from torchtyping import TensorType

# https://neetcode.io/problems/handwritten-digit-classifier
class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        self.first_layer = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.output_layer = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()
        pass
        # Define the architecture here

    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        return self.sigmoid(
            self.output_layer(self.dropout(self.relu(self.first_layer(images))))
        )
        pass
        # Return the model's prediction to 4 decimal places
