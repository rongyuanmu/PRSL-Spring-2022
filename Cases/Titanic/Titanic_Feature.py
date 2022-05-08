import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from sklearn import model_selection, decomposition
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.
import warnings
warnings.filterwarnings('ignore') #无视所有代码警告

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# Combine datasets
all_data = pd.concat([train, test], ignore_index=True)

# I. Fill NAN
# 1. Age (177)
# Get Title
all_data['Title'] = all_data['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
Title_Dict = {}
Title_Dict.update(dict.fromkeys(['Capt', 'Col', 'Major', 'Dr', 'Rev'], 'Officer'))
Title_Dict.update(dict.fromkeys(['Don', 'Sir', 'the Countess', 'Dona', 'Lady', 'Jonkheer'], 'Royalty'))
Title_Dict.update(dict.fromkeys(['Mme', 'Ms', 'Mrs'], 'Mrs'))
Title_Dict.update(dict.fromkeys(['Mlle', 'Miss'], 'Miss'))
Title_Dict.update(dict.fromkeys(['Mr'], 'Mr'))
Title_Dict.update(dict.fromkeys(['Master'], 'Master'))
all_data['Title'] = all_data['Title'].map(Title_Dict)
# Get Medium Number of each Title
grouped = all_data.groupby(['Title'])
median = grouped.Age.median()
# print(median)
# Fill nan
for i in range(len(all_data['Age'])):
    if pd.isnull(all_data['Age'][i]):
        all_data['Age'][i] = median[all_data['Title'][i]]
# 2. Fill nan Fare (1)
# Get P3 Medium Fare to Fill nan
P3med = all_data['Fare'].where(all_data['Pclass'] == 3).median()
for i in range(len(all_data['Fare'])):
    if pd.isnull(all_data['Fare'][i]):
        all_data['Fare'][i] = P3med
# 3. Fill nan Embarked (2)
all_data['Embarked'] = all_data['Embarked'].fillna('S')
# 4. Fill nan Cabin (687)
all_data['Cabin'] = all_data['Cabin'].fillna('U')

# II.Numerical
# 1. Title
all_data.loc[all_data['Title'] == 'Mr', 'Title'] = 0
all_data.loc[all_data['Title'] == 'Miss', 'Title'] = 1
all_data.loc[all_data['Title'] == 'Mrs', 'Title'] = 2
all_data.loc[all_data['Title'] == 'Master', 'Title'] = 3
all_data.loc[all_data['Title'] == 'Officer', 'Title'] = 4
all_data.loc[all_data['Title'] == 'Royalty', 'Title'] = 5
all_data['Title'] = all_data['Title'].astype('int64')
# 2. Sex
all_data.loc[all_data['Sex'] == 'male', 'Sex'] = 0
all_data.loc[all_data['Sex'] == 'female', 'Sex'] = 1
all_data['Sex'] = all_data['Sex'].astype('int64')
# 3. Ticket
Ticket_Count = dict(all_data['Ticket'].value_counts())
all_data['TicketGroup'] = all_data['Ticket'].apply(lambda x: Ticket_Count[x])
sns.barplot(x='TicketGroup', y='Survived', data=all_data)


def Ticket_Label(s):
    if (s >= 2) & (s <= 4):
        return 2
    elif ((s > 4) & (s <= 8)) | (s == 1):
        return 1
    elif (s > 8):
        return 0


all_data['TicketGroup'] = all_data['TicketGroup'].apply(Ticket_Label)
all_data['TicketGroup'] = all_data['TicketGroup'].astype('int64')
# 4. Cabin
all_data['Deck'] = all_data['Cabin'].str.get(0)
all_data.loc[all_data['Deck'] == 'A', 'Deck'] = 0
all_data.loc[all_data['Deck'] == 'B', 'Deck'] = 1
all_data.loc[all_data['Deck'] == 'C', 'Deck'] = 2
all_data.loc[all_data['Deck'] == 'D', 'Deck'] = 3
all_data.loc[all_data['Deck'] == 'E', 'Deck'] = 4
all_data.loc[all_data['Deck'] == 'F', 'Deck'] = 5
all_data.loc[all_data['Deck'] == 'G', 'Deck'] = 6
all_data.loc[all_data['Deck'] == 'T', 'Deck'] = 7
all_data.loc[all_data['Deck'] == 'U', 'Deck'] = 8
all_data['Deck'] = all_data['Deck'].astype('int64')
# 5. Embarked
all_data.loc[all_data['Embarked'] == 'S', 'Embarked'] = 0
all_data.loc[all_data['Embarked'] == 'C', 'Embarked'] = 1
all_data.loc[all_data['Embarked'] == 'Q', 'Embarked'] = 2
all_data['Embarked'] = all_data['Embarked'].astype('int64')
# 6. Family Scale
all_data['FamilySize'] = all_data['Parch'] + all_data['SibSp'] + 1
sns.barplot(x="FamilySize", y="Survived", data=all_data)


def FamilyScale(s):
    if (s >= 2) & (s <= 4):
        return 2
    elif ((s > 4) & (s <= 7)) | (s == 1):
        return 1
    elif (s > 7):
        return 0


all_data['FamilyScale'] = all_data['FamilySize'].apply(FamilyScale)
all_data['FamilyScale'] = all_data['FamilyScale'].astype('int64')

# III. Initial
# all_data.info()
train, test = all_data[:891], all_data[891:]
train_data, train_target = train.drop('Survived', axis=1), train['Survived']
train_data.pop('Name')
train_data.pop('Ticket')
train_data.pop('Cabin')
train_data.pop('PassengerId')
train_data.info()


# IV. Feature Importance
def rf_classifier(data, target, test, predictors):
    # predictors =  ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'TicketGroup', 'Deck', 'FamilySize', 'FamilyScale']
    data, test = data[predictors], test[predictors]
    data.info()
    data_train, data_validation, target_train, target_validation = train_test_split(data, target, test_size=0.3, random_state=12345)
    clf = RandomForestClassifier(random_state=10, n_estimators=26, max_depth=6)
    clf.fit(data_train, target_train)
    test_accuracy = clf.score(data_validation, target_validation) * 100
    print("Accuracy: %s%%." % test_accuracy)

# 0. All Features
print("-----------")
rf_classifier(train_data, train_target, test, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'TicketGroup', 'Deck', 'FamilySize', 'FamilyScale'])
print("-----------")
rf_classifier(train_data, train_target, test, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'TicketGroup', 'Deck'])
# 1. Random Forest Feature Importance
forest = RandomForestClassifier(random_state=10, n_estimators=26, max_depth=6)
forest.fit(train_data, train_target)
importance = forest.feature_importances_
indices = np.argsort(importance)[::-1]
feature_name = train_data.columns.values
for i in range(len(indices)):
    print(feature_name[indices[i]], importance[indices[i]])
# rf_classifier(train_data, train_target, test, ['Sex', 'Title'])
# rf_classifier(train_data, train_target, test, ['Pclass', 'Sex', 'Age', 'Fare', 'Title', 'Deck'])

# 2. Correlation coefficient
corrDf = all_data.corr()
res = corrDf['Survived'].sort_values(ascending=False)
print(res)
# rf_classifier(train_data, train_target, test, ['Sex', 'Title', 'TicketGroup', 'Pclass', 'Deck'])
# rf_classifier(train_data, train_target, test, ['Title', 'Sex', 'Deck', 'TicketGroup', 'Pclass', 'FamilyScale', 'Fare'])
rf_classifier(train_data, train_target, test, ['Pclass', 'Sex', 'Age', 'Fare', 'Title', 'Deck', 'FamilyScale'])