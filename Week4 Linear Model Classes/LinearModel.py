import numpy as np
import matplotlib.pyplot as plt

class LinearModel:
    def __init__(self, data, target, learning_rate, threshold, iteration):
        self.data = data
        self.target = target
        self.alpha = learning_rate
        self.iteration = iteration
        self.threshold = threshold
        self.weight = 0.1 * np.random.rand(len(self.data[0]), 1)
        self.cost = np.zeros(0)

    def LeastSquare(self):
        for _ in range(self.iteration):
            gradient = (2 / len(self.data)) * np.dot(np.transpose(self.data), (np.dot(self.data, self.weight) - self.target))
            cost_current = (1 / len(self.data)) * np.linalg.norm(self.target - np.dot(self.data, self.weight))
            self.cost = np.append(self.cost, cost_current)
            if cost_current < self.threshold:
                break
            else:
                self.weight = self.weight - self.alpha * gradient
        plt.plot(self.cost)
        plt.show()
        print(self.cost)
        return self.weight

    def Perceptron(self):
        sign = self.target * 2 - 1
        for _ in range(self.iteration):
            gradient = np.zeros(len(self.data[0]))
            cost_tmp = 0
            cost_current = (sign * np.dot(self.data, self.weight))
            for i in range(len(self.data)):
                if (cost_current[i] < 0).all():
                    gradient = gradient - sign[i] * np.transpose(self.data[i])
                    cost_tmp = cost_tmp - cost_current[i]
            cost_tmp = (1 / np.linalg.norm(self.weight)) * cost_tmp
            self.cost = np.append(self.cost, cost_tmp)
            gradient = gradient.reshape(-1, 1)
            if (cost_tmp <= self.threshold).all():
                break
            else:
                self.weight = self.weight - self.alpha * gradient
        plt.plot(self.cost)
        plt.show()
        return self.weight

    def LogisticRegression(self):

        return self.weight


