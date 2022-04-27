from sklearn import tree
from matplotlib import pyplot as plt
import numpy as np

# Category      0         1           2
# Outlook[0]    Sunny     Overcast    Rain
# Temperature[1]Hot       Mild        Cold
# Humidity[2]   High      Normal
# Wind[3]       Weak      Strong
# Play Tennis   No        Yes

data = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 2, 1, 0],
    [2, 2, 1, 1],
    [1, 2, 1, 1],
    [0, 1, 0, 0],
    [0, 2, 1, 0],
    [2, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [2, 1, 0, 1]
])
target = np.array([
    [0],
    [0],
    [1],
    [1],
    [1],
    [0],
    [1],
    [0],
    [1],
    [1],
    [1],
    [1],
    [1],
    [0]
])
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf.fit(data, target)
tree.plot_tree(clf)
plt.show()