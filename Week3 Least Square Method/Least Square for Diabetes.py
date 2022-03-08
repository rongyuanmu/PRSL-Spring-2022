import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, model_selection

# Load Datasets
diabetes = datasets.load_diabetes()
data = diabetes.data
y = diabetes.target
# Get parameters of dataset
data_num, feature_num = data.shape
# Feature Scaling (Mean Normalization)
mean = np.zeros(feature_num)
mean = np.average(data, axis=0)
ptp = np.zeros(feature_num)
ptp = np.ptp(data, axis=0)
for i in range(feature_num):
    for j in range(data_num):
        data[j][i] = (data[j][i] - mean[i]) / ptp[i]

# Extend X0=1 Column
X = np.ones([data_num, feature_num + 1])
for i in range(data_num):
    for j in range(feature_num):
        X[i][j + 1] = data[i][j]

# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=8, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test

# Least Square Algorithm
def LeastSquare(data, target):
    # Iteration Method
    row, col = data.shape
    target = np.transpose(np.array([target]))
    # Initial Learning rate, Threshold, Iteration
    alpha = 0.001
    threshold = 0.01
    iteration = 1000

    # Initial Beta
    beta = np.random.rand(col, 1)
    # negative-delta = X^T · Y - X^T * X * beta
    delta = np.dot(np.transpose(data), target) - np.dot(np.dot(np.transpose(data), data), beta)
    beta_new = beta + alpha * delta
    loss = np.zeros(iteration)
    for i in range(iteration):
        loss[i] = np.linalg.norm(target - np.dot(data, beta_new))
        if loss[i] < threshold:
            break
        else:
            beta = beta_new
            delta = np.dot(np.transpose(data), target) - np.dot(np.dot(np.transpose(data), data), beta)
            beta_new = beta + alpha * delta
    plt.plot(loss)
    plt.show()
    # Normal Equation: beta = (X^T · X)^(-1) · (X^T · Y)
    #beta = np.dot(np.linalg.inv(np.dot(np.transpose(data), data)), np.dot(np.transpose(data), target))
    return beta

# Validation
def Validation(data, target, beta):
    a, b = data.shape
    # Cover beta to column vector
    theta = np.transpose(np.array([beta]))
    # Calculate Y Hat
    Y_hat = np.dot(data, theta)
    # RMSE = Sqrt(1/N * Sigma[(yi - yi_hat)^2])
    temp = 0
    for i in range(a):
        temp = temp + (Y_hat[i] - target[i]) ** 2
    RMSE = np.sqrt(temp / a)
    return RMSE


# Call functions
data_train, target_train, data_test, target_test = kfold(X, y)
beta = LeastSquare(data_train, target_train)
RMSE = Validation(data_test, target_test, beta)
print('RMSE of this estimation: %f' %float(RMSE))
