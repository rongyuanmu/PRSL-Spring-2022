import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
data = iris.data
target = iris.target
print(data.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[0:50, 0], data[0:50, 1], data[0:50, 2],
           marker='x', color='blue', s=40, label='Setosa')
ax.scatter(data[50:100, 0], data[50:100, 1], data[50:100, 2],
           marker='o', color='green', s=40, label='Versicolour')
ax.scatter(data[100:150, 0], data[100:150, 1], data[100:150, 2],
           marker='^', color='red', s=40, label='Virginica')
ax.set_xlabel('Sepal length (cm)')
ax.set_ylabel('Sepal width (cm)')
ax.set_zlabel('Petal length (cm)')
plt.title('Iris Dataset')
plt.show()

data = data[:, [0, 1, 2]]
