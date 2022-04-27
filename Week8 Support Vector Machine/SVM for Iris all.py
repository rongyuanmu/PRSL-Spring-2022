import numpy as np
from sklearn import datasets,model_selection
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# Data import and process
iris = datasets.load_iris()
data = iris.data
target = iris.target.reshape(-1, 1)
data = np.c_[np.ones(len(data)), data]


# K-Fold
def kfold(data, target):
    kf = model_selection.KFold(n_splits=5, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test


# SVM
def SVM(data, target):

    return 0

data_train, target_train, data_test, target_test = kfold(data, target)
svm = SVC()
svm.fit(data_train, target_train)
pred = svm.predict(data_test)
acc = accuracy_score(target_test, pred)
print(acc)
