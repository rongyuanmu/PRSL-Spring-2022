import numpy as np
from sklearn import model_selection, datasets
import scipy.stats as st

# import dataset_iris from sklearn-datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
a, b = X.shape
dataset = np.zeros([a, b+1])
for i in range(a):
    dataset[i][0] = y[i]
    for j in range(b+1):
        if j != 0:
            dataset[i][j] = X[i][j-1]
# K-Fold
np.random.shuffle(dataset)
kf = model_selection.KFold(n_splits=5, shuffle=True)
for train_idx, test_idx in kf.split(dataset):
    data_train = dataset[train_idx]
    data_test = dataset[test_idx]
print(data_train)

# Divide Dataset into Target and Features
def divTarFea(arr):
    row = len(arr)
    col = len(arr[0]) - 1
    target = np.zeros(row)
    for i in range(row):
        target[i] = arr[i][0]
    feature = np.zeros([row, col])
    for i in range(row):
        for j in range(col):
            feature[i][j] = arr[i][j + 1]
    return row, col, target, feature

# Naive Bayes Algorithm
def NaiveBayes(arr):
    # Dataset for Train Process
    data_num, feature_num, target, feature = divTarFea(arr)
    for i in range(data_num):
        for j in range(feature_num):
            feature[i][j] = arr[i][j + 1]
    # Number of Unique Target
    label = np.unique(target)
    label_num = label.size
    # Calculate Prior Probability
    prior = np.zeros(label_num)
    for i in range(label_num):
        temp = np.sum(target == label[i])
        prior[i] = temp / data_num
    # Calculate mean, standard deviation of features
    mean = np.zeros([label_num, feature_num])
    std = np.zeros([label_num, feature_num])
    for i in range(label_num):
        tmp_index = np.where(target == label[i])[0]
        for j in range(feature_num):
            tmp = np.zeros([1, len(tmp_index)])
            for k in range(len(tmp_index)):
                tmp[0][k] = feature[tmp_index[k]][j]
            mean[i][j] = np.mean(tmp)
            std[i][j] = np.std(tmp)
    return prior, mean, std, label_num


# Gaussian Distribution Estimate
def BayesClassification(feature, prior, mean, std, labelnum):
    row, col = feature.shape
    post = np.zeros([row, labelnum])
    estimate = np.zeros(row)
    for i in range(row):
        for j in range(labelnum):
            p_product = 1
            for k in range(col):
                p_product = p_product * st.norm.pdf(feature[i][k], mean[j][k], std[j][k])
            post[i][j] = p_product * prior[j]
        estimate[i] = np.argmax(post[i])
    return estimate

# Call functions
prior, mean, std, label_num = NaiveBayes(data_train)
test_num, fea_num, label, score = divTarFea(data_test)
estmation = BayesClassification(score, prior, mean, std, label_num)
# Validation
right_num = estmation == label
rigth_rate = np.sum(right_num) / test_num
print('The accuracy is {:.2%}.'.format(rigth_rate))
