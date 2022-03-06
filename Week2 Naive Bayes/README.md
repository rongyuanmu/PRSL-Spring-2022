@@ -0,0 +1,132 @@
# 问题：性别分类
1. 训练样本：
2. 测试样本：
# 解答：
### Import Packages
导包。
```
import numpy as np
from sklearn import model_selection
import scipy.stats as st
```
### Import dataset manually [Gender(0 for female, 1 for male) height(feet) weight(lbs) foot size(inches)]
首先手动输入数据，并转化成数组形式存放。
```
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
```
### K-Fold
使用K折交叉验证对数据集进行随机划分，因为数据集内容较少，本次使用3折。
```
np.random.shuffle(dataset)
kf = model_selection.KFold(n_splits=3, shuffle=False)
for train_idx, test_idx in kf.split(dataset):
    data_train = dataset[train_idx]
    data_test = dataset[test_idx]
print(data_train)
```
得到训练集：<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/ROC%20Curve.png)
### 函数1：将数组数据切分。
得到标签（target）与特征（feature）两个数组，以及数据数量、特征维度。
```
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
```

### 函数2：计算
得到先验概率、特征向量的均值（mean）和标准差（std）
```
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
```
### 函数3：分类
根据得到的均值和标准差创建高斯分布，然后利用朴素贝叶斯进行分类。
```
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
```
### 调用函数
```
prior, mean, std, label_num = NaiveBayes(data_train)
test_num, fea_num, label, score = divTarFea(data_test)
estmation = BayesClassification(score, prior, mean, std, label_num)
# Validation
right_num = estmation == label
rigth_rate = np.sum(right_num) / test_num
print('The accuracy is {:.2%}.'.format(rigth_rate))
```
因为对数据集进行了乱序处理后，再进行了K折交叉验证，所以每次分配的训练集和测试集内容不同，导致每次准确率的不同。
<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/ROC%20Curve.png)
### 估计
```
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
```
使用测试样本与我自己的实际数据进行测试：<br>
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/ROC%20Curve.png)