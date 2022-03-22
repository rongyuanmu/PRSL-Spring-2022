import numpy as np
from sklearn import model_selection


def FileReader(address):
    data = np.loadtxt(address, skiprows=1, delimiter=',')
    return data


def PreProcess(raw):
    target = raw[:, 0]
    label = np.unique(target)
    data = raw[:, 1:]
    # Compute brightness ratio (0 for Dark, 1 for Bright)
    data = data / 255
    data_plt = data.reshape(data.shape[0], np.int64(np.sqrt(data.shape[1])), np.int64(np.sqrt(data.shape[1])), 1)
    return data, target, data_plt, label


# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=10, shuffle=True)
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


fashion_data = FileReader(f"fashion-mnist_test.csv")
data, target, data_plt, label = PreProcess(fashion_data)
data_train, target_train, data_test, target_test = kfold(data, target)
predict = KNN(data_train, target_train, data_test, 6.8, 1, label)
accuracy = Validation(predict, target_test)
print(accuracy)
