# 问题：
对sklearn.datasets.iris数据进行线型感知机分类
1. 使用前两类花setosa(50), versicolour(50)中Sepal Length, Sepal Length；
2. 构造模型；
3. 画图。
# 解答：
### Import Packages
导包。
```
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
```
### Load datasets from sklearn
从包内获取数据集及其参数。
```
iris = datasets.load_iris()
# Iris: setosa(50), versicolour(50)
X = iris.data[0:100]
X = X[:, [0,1]]
print(X.shape)
y = iris.target.reshape(-1, 1)[0:100]
X = np.c_[np.ones(len(X)), X]
```
### Perceptron Function
```
def perceptron(data, target):
    row, col = data.shape
    sign = target * 2 - 1
    # Initial w
    w = 0.01 * np.random.rand(col, 1)
    # First Calculate
    result = np.dot(data, w)
    pred = 1 * (result > 0)
    # Define Super Parameters
    eta = 0.01
    iteration = 0
    error = []
    # Iteration
    while np.sum(pred != target) and iteration < 5000:
        # Find Wrong Classification
        flag = np.array((pred != target)).reshape(-1)
        X_error = X[flag, :]
        y_error = sign[flag, :]
        # Derivative of w
        delta_w = np.dot(X_error.T, y_error)
        w_new = w + eta * delta_w
        # Error formula
        error.append((- 1 / np.linalg.norm(w)) * (np.dot((np.dot(X_error, w)).T, y_error)))
        # Prepare for next iteration
        iteration = iteration + 1
        pred = []
        w = w_new
        result = np.dot(data, w)
        pred = 1 * (result > 0)
    print(iteration)
    return w, error
```
### Call function
```
# Call function
w, error = perceptron(X, y)
error = np.array(error).reshape(-1)
```
### Plot
1. Plot Error Img
```
plt.plot(error)
plt.show()
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week3%20Perceptron/Ouput/Error%20Img.png)
<br>
2. Plot Data distribution and Decision boundary
```
x = np.arange(4, 8)
y = -w[0] / w[2] - w[1] / w[2] * x
plt.plot(x, y)
plt.scatter(X[0:50, 1], X[0:50, 2], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 1], X[50:100, 2], color='blue', marker='x', label='versicolour')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week3%20Perceptron/Ouput/Decision%20Boundary.png)
