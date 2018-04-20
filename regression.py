import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:

    def __init__(self, alpha=0.0001, iteration=100000, feature_count=1):
        self.alpha = alpha
        self.iteration = iteration
        self.theta = np.array([0] * (feature_count + 1))
        self.costs = []

    def fit(self, X, Y):
        self.costs = [0] * self.iteration
        m = len(Y)

        for iteration in range(self.iteration):
            self.theta = self.theta - self.alpha * X.T.dot(X.dot(self.theta) - Y) / m
            cost = self.cost_function(X, Y, self.theta)
            self.costs[iteration] = cost

        print(self.theta)

    def cost_function(self, X, Y, B):
        m = len(Y)
        J = np.sum((X.dot(B) - Y) ** 2) / (2 * m)
        return J

    def predict(self, X):
        return self.theta.dot(X)

    def plot(self):
        x = range(self.iteration)
        plt.scatter(self.costs, x)
        plt.show()
