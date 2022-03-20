import numpy as np
from sklearn import datasets, model_selection
import matplotlib.pyplot as plt

# Load Iris dataset and Select 2 flowers to classify
X = datasets.load_iris().data
y = datasets.load_iris().target.reshape(-1, 1)
X = X[0:100]
y = y[0:100]
X = np.c_[np.ones(len(X)), X]


# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=5, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test


# Sigmoid Function
def Sigmoid(z):
    return 1.0 / (1 + np.exp(z))


# Logistic Regression
def LogisticRegression(data, target):
    # Get data parameters
    data_num, feature_num = data.shape
    # Initial super parameter
    alpha = 0.01
    iteration = 5000
    threshold = 0.01
    theta = 0.01 * np.random.rand(feature_num, 1)
    cost = np.zeros(iteration)
    # First Iteration
    delta_theta = - (1 / data_num) * np.dot(np.transpose(data), (Sigmoid(np.dot(data, theta)) - target))
    theta_new = theta + alpha * delta_theta
    for i in range(iteration):
        cost_tmp = 0
        for j in range(data_num):
            cost_tmp = cost_tmp - target[j] * np.log(Sigmoid(np.dot(data[j], theta))) - (1 - target[j]) * np.log(
                1 - Sigmoid(np.dot(data[j], theta)))
        cost[i] = cost_tmp / data_num
        if cost[i] < threshold:
            break
        else:
            theta = theta_new
            delta_theta = (1 / data_num) * np.dot(np.transpose(data), (Sigmoid(np.dot(data, theta)) - target))
            theta_new = theta + alpha * delta_theta
    plt.plot(cost)
    plt.show()
    return theta


# Validation
def Validation(data, target, theta):
    p = np.zeros(len(data))
    for i in range(len(data)):
        posibility = Sigmoid(- np.dot(data[i], theta))
        if posibility <= 0.5:
            p[i] = 1
        else:
            p[i] = 0
    target = target.reshape(-1)
    correct = np.sum(p == target)
    accuracy = correct / len(data)
    return accuracy


# Call functions
data_train, target_train, data_test, target_test = kfold(X, y)
theta = LogisticRegression(data_train, target_train)
accuracy = Validation(data_test, target_test, theta)
print('The accuracy is {:.2%}.'.format(accuracy))
