from sklearn import datasets
import DataProcess as dp
import LinearModel as lm
import numpy as np
import matplotlib.pyplot as plt




iris = datasets.load_iris()
X = iris.data[0:100]
X = X[:, [0,1]]
y = iris.target[0:100]
a = dp.DataProcess(X, y)
c, d = a.ExtendX()
c, d = a.random()
b = lm.LinearModel(c, d, 0.1, 0.000001, 2500).Perceptron()

x = np.arange(4, 8)
y = -b[0] / b[2] - b[1] / b[2] * x
plt.plot(x, y)
plt.scatter(X[0:50, 0], X[0:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolour')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
