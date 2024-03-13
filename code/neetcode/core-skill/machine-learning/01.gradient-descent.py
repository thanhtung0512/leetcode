# https://neetcode.io/problems/gradient-descent


# The first step in gradient descent is to calculate the derivative (gradient) of the function. The derivative gives the slope of the function.
# Start with an initial guess. In this problem the initial guess is given as a parameter.
# At each step, the current value (or guess) is updated by subtracting the product of the derivative and the learning rate.
# This process is repeated (iterated) a variable number of times. Upon each iteration we will move closer to the point where the derivative is zero, which is the minimum of the function.

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        currentGuess = init;
        for i in range (0, iterations):
            gradient = 2 * currentGuess;
            currentGuess = currentGuess - learning_rate * gradient;
        return round(currentGuess,5);