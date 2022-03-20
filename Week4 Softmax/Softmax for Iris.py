import numpy as np
from sklearn import datasets, model_selection
import matplotlib.pyplot as plt

# Import iris datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)
X = np.c_[np.ones(len(X)), X]


# Random Function
def random(data, target):
    combine = np.hstack((data, target))
    np.random.shuffle(combine)
    data = combine[:, 0:-1]
    target = combine[:, -1].reshape(-1, 1)
    return data, target


# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=8, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test


# Calculate Soft Possibility
def SoftP(weight, data_1):
    z = np.dot(weight, data_1)
    e_z = np.exp(z)
    p = e_z / np.sum(e_z)
    return p


# Calculate Loss Function
def SoftLoss(weight, data, target):
    loss = 0
    for i in range(len(data)):
        pi = SoftP(weight, data[i])
        loss = loss - (target[i] * np.log(pi)).sum()
    return loss


# Softmax Algorithm
def SoftmaxFit(data, target, label):
    # Define Super Parameter
    eta = 0.01
    threshold = 0.001
    iteration = 8000
    cost = np.zeros(0)
    # Random initialization (3 * 5)
    weight = 0.1 * np.random.rand(len(np.unique(label)), len(data[0]))
    loss = SoftLoss(weight, data, target)
    cost = np.append(cost, loss)
    # Iteration
    for _ in range(iteration):
        # Select one data randomly
        stochastic = np.random.choice(len(data))
        data_current = data[stochastic].reshape(-1, 1)
        target_current = target[stochastic].reshape(-1, 1)
        p_current = SoftP(weight, data_current)
        gradient = np.dot((p_current - target_current), np.transpose(data_current))
        weight = weight - eta * gradient
        loss_new = SoftLoss(weight, data, target)
        if np.abs(loss - loss_new) <= threshold:
            cost = np.append(cost, loss_new)
            break
        else:
            loss = loss_new
            cost = np.append(cost, loss)
    print('Iteration: %d' %(len(cost)))
    plt.plot(cost)
    plt.show()
    return weight


# Validation
def Validation(weight, data, target):
    correct = 0
    for i in range(len(data)):
        pi = SoftP(weight, data[i])
        flag = (pi * target[i]).sum()
        if flag == max(pi):
            correct = correct + 1
    acc = correct / len(data)
    return acc


# Data Process
data, target = random(X, y)
data_train, target_train, data_test, target_test = kfold(data, target)

# Encode y into One-hot format
target_train = target_train.reshape(-1).astype('int64')
target_train = np.eye(len(np.unique(y)))[target_train]

target_test = target_test.reshape(-1).astype('int64')
target_test = np.eye(len(np.unique(y)))[target_test]

# Fit
weight = SoftmaxFit(data_train, target_train, target)
accuracy = Validation(weight, data_test, target_test)
print('Accuracy: {:.2%}.' .format(accuracy))