import pandas as pd
import numpy as np


class LinearRegression:

    def __init__(self, alpha=0.0001, iteration=100000, feature_count=1):
        self.alpha = alpha
        self.iteration = iteration
        self.theta = np.array([0] * (feature_count + 1))
        self.cost_history = []

    def fit(self, X, Y):
        self.cost_history = [0] * self.iteration
        m = len(Y)

        for iteration in range(self.iteration):
            # Hypothesis Values
            h = X.dot(self.theta)
            # Difference between Hypothesis and Actual Y
            loss = h - Y
            # Gradient Calculation
            gradient = X.T.dot(loss) / m
            # Changing Values of theta using Gradient
            self.theta = self.theta - self.alpha * gradient
            # New Cost Value
            cost = self.cost_function(X, Y, self.theta)
            self.cost_history[iteration] = cost

    def cost_function(self, X, Y, B):
        m = len(Y)
        J = np.sum((X.dot(B) - Y) ** 2) / (2 * m)
        return J

    def predict(self, X):
        return self.theta.dot(X)
