import numpy as np
from numpy.typing import NDArray

# https://neetcode.io/problems/linear-regression-training

class Solution:
    def get_derivative(
        self,
        model_prediction: NDArray[np.float64],
        ground_truth: NDArray[np.float64],
        N: int,
        X: NDArray[np.float64],
        desired_weight: int,
    ) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(
        self, X: NDArray[np.float64], weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self,
        X: NDArray[np.float64],
        Y: NDArray[np.float64],
        num_iterations: int,
        initial_weights: NDArray[np.float64],
    ) -> NDArray[np.float64]:
        for i in range(0, num_iterations):
            predicts = self.get_model_prediction(X, initial_weights)
            for j in range(0, 3):

                gradient = self.get_derivative(predicts, Y, len(X), X, j)
                initial_weights[j] = initial_weights[j] - self.learning_rate * gradient

        return np.round(initial_weights, 5)
        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)
        pass
