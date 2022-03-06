import numpy as np
from sklearn import model_selection
import scipy.stats as st

# import dataset manually
# Gender(0 for female, 1 for male) height(feet) weight(lbs) footsize(inches)
dataset = [
    [1, 6, 180, 12],
    [1, 5.92, 190, 11],
    [1, 5.58, 170, 12],
    [1, 5.92, 165, 10],
    [0, 5, 100, 6],
    [0, 5.5, 150, 8],
    [0, 5.42, 130, 7],
    [0, 5.75, 150, 9]
]
dataset = np.array(dataset)

# K-Fold
np.random.shuffle(dataset)
kf = model_selection.KFold(n_splits=3, shuffle=False)
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

# Estimator for user
print("How many person you want to estimate?")
person = int(input())
data_user = np.zeros([person, fea_num])
print('Personal Data (feet weight footsize) and new line for another:')
for i in range(person):
    data_user[i] = input().split(" ")
result_user = BayesClassification(data_user, prior, mean, std, label_num)
for i in range(person):
    print('A person whose height is %.2f feet, weight is %.2f lbs, foot size is %.2f inches is inferred to be a'%(data_user[i][0], data_user[i][1], data_user[i][2]), end=" ")
    if result_user[i] == 0:
        print('female')
    else:
        print('male')
print(result_user)
