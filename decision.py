import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('files/titanic.csv', usecols=['Pclass', 'Age', 'Sex', 'Fare', 'Survived'])\
    .dropna().reset_index().replace('female', 0).replace('male', 1)
X = data[['Pclass', 'Age', 'Sex', 'Fare']]
Y = data[['Survived']]
clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, Y)
ips = clf.feature_importances_
result = {}
i = 0
for key in X:
    result[key] = ips[i]
    i += 1
key_max_value_01 = max(result, key=result.get)
del result[key_max_value_01]
key_max_value_02 = max(result, key=result.get)
f = open('result.txt', 'w', encoding='ascii')
f.write(key_max_value_01)
f.writelines(',')
f.writelines(key_max_value_02)
f.close()
