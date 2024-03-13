# https://neetcode.io/problems/gradient-descent
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        currentGuess = init;
        for i in range (0, iterations):
            gradient = 2 * currentGuess;
            currentGuess = currentGuess - learning_rate * gradient;
        return round(currentGuess,5);