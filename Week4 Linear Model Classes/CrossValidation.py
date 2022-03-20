from sklearn import model_selection


class CrossValidation:
    def __init__(self, data, target, splits, shuffle):
        self.data = data
        self.target = target
        self.splits = splits
        self.shuffle = shuffle

    def KFold(self):
        kf = model_selection.KFold(n_splits=self.splits, shuffle=self.shuffle)
        for train_idx, test_idx in kf.split(self.data, self.target):
            data_train = self.data[train_idx]
            target_train = self.target[train_idx]
            data_test = self.data[test_idx]
            target_test = self.target[test_idx]
        return data_train, target_train, data_test, target_test
