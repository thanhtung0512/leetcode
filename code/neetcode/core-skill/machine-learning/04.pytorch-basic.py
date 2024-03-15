import torch
import torch.nn
from torchtyping import TensorType


# https://neetcode.io/problems/basics-of-pytorch


# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html


# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # torch.reshape() will be useful - check out the documentation
        M = to_reshape.shape[0]
        N = to_reshape.shape[1]
        new_row = M * N // 2
        return to_reshape.reshape(new_row, 2)
        pass

    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # torch.mean() will be useful - check out the documentation
        return torch.mean(to_avg, 0)
        pass

    def concatenate(
        self, cat_one: TensorType[float], cat_two: TensorType[float]
    ) -> TensorType[float]:
        # torch.cat() will be useful - check out the documentation
        M = cat_one.shape[0]
        N = cat_two.shape[1]
        return torch.cat((cat_one, cat_two), -1)
        pass

    def get_loss(
        self, prediction: TensorType[float], target: TensorType[float]
    ) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        return torch.nn.functional.mse_loss(prediction, target)
        pass
