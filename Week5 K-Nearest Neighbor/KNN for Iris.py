import numpy as np
from sklearn import model_selection, datasets


def PreProcess(raw):
    target = raw.target
    label = np.unique(target)
    data = raw.data
    return data, target, label


# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=3, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test


def Distance(a, b):
    dif = a - b
    manhattan = np.linalg.norm(dif, ord=1)
    euler = np.linalg.norm(dif, ord=2)
    chebyshev = np.linalg.norm(dif, ord=np.inf)
    return manhattan, euler, chebyshev


def KNN(data_train, target_train, data_test, k, distance_i, label):
    predict = np.zeros(len(data_test))
    for i in range(len(data_test)):
        count = np.zeros(len(label))
        for j in range(len(data_train)):
            dist_tmp = Distance(data_test[i], data_train[j])[distance_i]
            if dist_tmp <= k:
                neighbor = np.int64(target_train[j])
                count[neighbor] = count[neighbor] + 1
        predict[i] = np.argmax(count)
    return predict


def Validation(predict, target):
    correct = np.sum(predict == target)
    accuracy = correct / len(target)
    return accuracy


iris = datasets.load_iris()
data, target, label = PreProcess(iris)
data_train, target_train, data_test, target_test = kfold(data, target)
print(data_train.shape)
predict = KNN(data_train, target_train, data_test, 2, 1, label)
accuracy = Validation(predict, target_test)
print(accuracy)
