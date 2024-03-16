import torch
import torch.nn as nn
from torchtyping import TensorType


# https://neetcode.io/problems/sentiment-analysis
class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.embedding_layer = nn.Embedding(vocabulary_size, 16)
        self.linear_layer = nn.Linear(16, 1)
        self.sigmoid_layer = nn.Sigmoid()
        pass

    def forward(self, x: TensorType[int]) -> TensorType[float]:
        # Hint: The embedding layer outputs a B, T, embed_dim tensor
        # but you should average it into a B, embed_dim tensor before using the Linear layer
        embedding = self.embedding_layer(x)
        mean_embedding = torch.mean(embedding, axis=1)

        projected = self.linear_layer(mean_embedding)
        result = self.sigmoid_layer(projected)
        return torch.round(result, decimals=4)
        # Return a B, 1 tensor and round to 4 decimal places
        pass
