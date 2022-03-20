import numpy as np


class DataProcess:
    def __init__(self, data, target):
        self.data = data
        self.target = target.reshape(-1, 1)

    def ExtendX(self):
        data_num, feature_num = self.data.shape
        self.data = np.c_[np.ones(data_num), self.data]
        return self.data, self.target

    def random(self):
        combine = np.hstack((self.data, self.target))
        np.random.shuffle(combine)
        self.data = combine[:, 0:-1]
        self.target = combine[:, -1].reshape(-1, 1)
        return self.data, self.target
