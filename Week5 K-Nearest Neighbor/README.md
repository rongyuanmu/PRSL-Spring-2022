# 问题：运用最近邻分类器对Fashion MNIST数据进行分类
1. 由于数据量大，我们仅对Fashion MNIST的测试集进行分类实验
2. Fashion MNIST测试集： 数据包含十类，每类1000个样本，每个样本为28 * 28 的图像
3. 实验要求：对数据集划分训练集和验证集
4. 用训练集使用sklearn的KNeighborsClassifier训练的到分类器
5. 用得到的分类器对验证集的数据进行分类，得到准确率
# 解答：
### Import Packages
导包。
```
import numpy as np
from sklearn import model_selection
```
### Function1: FileReader
读取目录下的csv文件，并以数组形式返回。
```
def FileReader(address):
    data = np.loadtxt(address, skiprows=1, delimiter=',')
    return data
```
### Function2: PreProcess Data
target: 每条数据分类标签
label: 数据标签
data: 每条数据的值
data_plt: 用于调用plt画出该条数据的图像
```
def PreProcess(raw):
    target = raw[:, 0]
    label = np.unique(target)
    data = raw[:, 1:]
    # Compute brightness ratio (0 for Dark, 1 for Bright)
    data = data / 255
    data_plt = data.reshape(data.shape[0], np.int64(np.sqrt(data.shape[1])), np.int64(np.sqrt(data.shape[1])), 1)
    return data, target, data_plt, label
```
### Function3: K-Fold
使用Cross Validation - KFold 方法对数据集划分。
```
def kfold(data, target):
    kf = model_selection.KFold(n_splits=8, shuffle=True)
    for train_idx, test_idx in kf.split(data, target):
        data_train = data[train_idx]
        target_train = target[train_idx]
        data_test = data[test_idx]
        target_test = target[test_idx]
    return data_train, target_train, data_test, target_test
```
### Function4: Compute Distance
返回两个向量之间不同的距离（曼哈顿、欧拉、切比雪夫）。
```
def Distance(a, b):
    dif = a - b
    manhattan = np.linalg.norm(dif, ord=1)
    euler = np.linalg.norm(dif, ord=2)
    chebyshev = np.linalg.norm(dif, ord=np.inf)
    return manhattan, euler, chebyshev
```
### Function5: KNN Algorithm
选择K近邻中，含有最多的类别作为预测。
```
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
```
### Function6: Validation
计算Accuracy 。
```
def Validation(predict, target):
    correct = np.sum(predict == target)
    accuracy = correct / len(target)
    return accuracy
```
### Call functions
```
fashion_data = FileReader(f"fashion-mnist_test.csv")
data, target, data_plt, label = PreProcess(fashion_data)
data_train, target_train, data_test, target_test = kfold(data, target)
predict = KNN(data_train, target_train, data_test, 6.8, 1, label)
accuracy = Validation(predict, target_test)
print(accuracy)
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week5%20K-Nearest%20Neighbor/Output/KNN%20Accuracy.png)
