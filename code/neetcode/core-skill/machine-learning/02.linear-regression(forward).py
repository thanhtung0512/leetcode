import numpy as np
from numpy.typing import NDArray

# Linear Regression is a model that assumes a linear relationship within our dataset.

# For example, assume we are building a model to predict the price of Ubers, and we have a dataset of 100,000 Uber rides. For each data point, we have 3 attributes/features: the time of day of the ride, the length of the ride in miles, and the projected duration of the ride in minutes.

# By assuming a linear relationship, we think that the following equation is enough to resemble/model the relationship, meaning no exponents, logarithms or any other non-linear equations. If we had more attributes, we would have more weights too.
# price(x, y, z) = w1 * x + w2 * y + w3 * z

# Training a linear regression model is about finding the values of the weights, or the W's that make our price function's predictions close to the real answers in our dataset.

# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html


class Solution:

    def get_model_prediction(
        self, X: NDArray[np.float64], weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        res = np.matmul(X, weights)
        return np.round(res, 5)

    def get_error(
        self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]
    ) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        return np.round(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            np.mean(np.square(np.subtract(model_prediction, ground_truth))), 5
        )
