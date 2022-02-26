# 问题：
1. 针对以上的数据，将label为1的作为P类，把label为0的作为N类，阈值设为0.05时，计算混淆矩阵，计算TPR，FPR，Precision，Recall，F1-score，Accuracy
2. 绘制ROC曲线，计算AUC
# 解答：
### Import Packages
导包。
```
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay, auc
```
### Read file in folder
首先读取数据，并创建两个数组label、score进行存放。
```
with open('score.csv', newline='') as f:
    reader = csv.reader(f)
    s = list(reader)
tmp = s[0]
score = np.array([float(item) for item in tmp])

with open('label.csv', newline='') as f:
    reader = csv.reader(f)
    l = list(reader)
tmp = l[0]
label = np.array([float(item) for item in tmp])
```
### Predict Score
此处先设定一个阈值变量，并创建一个新的数组predict存放预测数据。
```
threshold = 0.05
predict = score.copy()
predict[predict>threshold] = 1
predict[predict<threshold] = 0
```

### Calculate confusion matrix, TPR，FPR，Precision，Recall，F1-score，Accuracy
利用包内函数，直接求出所需数据。
```
cm = confusion_matrix(label, predict)
print('Confusion Matrix: \n',cm)
accuracy = accuracy_score(label, predict)
print('Accuracy: ', accuracy)
precision = precision_score(label, predict)
print('Precision: ', precision)
recall = recall_score(label, predict)
print('Recall: ', recall)
f1 = f1_score(label, predict)
print('F1 score: ', f1)
tpr = cm[1][1]/(cm[0][0]+cm[1][1])
print('TruePositiveRate: ', tpr)
fpr = cm[0][1]/(cm[0][1]+cm[1][0])
print('FalsePositiveRate: ', fpr)
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/Data.png)
### Plot
首先画出混淆矩阵。
```
disp = ConfusionMatrixDisplay(cm)
disp.plot()
plt.show()
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/Confusion%20Matrix.png)
<br>
再画出ROC曲线与0.5曲线的对比图。
```
plt.figure()
fpr, tpr, threshold = metrics.roc_curve(label, score)
auc = auc(fpr, tpr)
plt.plot(
    fpr,
    tpr,
    color="red",
    label="ROC Curve (Area = '%0.2f')" % auc,
)
plt.plot([0,1],[0,1], color="blue", linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver Operating Characteristic")
plt.legend(loc="lower right")
plt.show()
```
![image](https://github.com/rongyuanmu/PRSL-Spring-2022/blob/main/Week%201/Output/ROC%20Curve.png)
