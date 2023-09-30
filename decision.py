import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

columns = ['col1', 'draw', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'sum_num', 'even']
# Data_645 = pd.read_excel('files/arch645.xlsx', names=columns, index_col=1)
Data_645 = pd.read_excel('files/arch645.xlsx')
Data_645 = Data_645.drop(['Unnamed: 0', 'Unnamed: 1'], axis=1)
Data_645 = Data_645.drop([0, 1, 2])
print(Data_645)
# X_train = Data_train.drop(columns='col1')
# y_train = Data_train['col1']
# Data_test = pd.read_csv('files/perceptron-test.csv', names=columns)
# X_test = Data_test.drop(columns='col1')
# y_test = Data_test['col1']
#
# clf = Perceptron(max_iter=5, tol=None, random_state=241)
#
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
#
# accuracy_test = accuracy_score(y_test, predictions)
#
# print(accuracy_test)
#
# scaler = StandardScaler()
# X_train_scaler = scaler.fit_transform(X_train)
# X_test_scaler = scaler.transform(X_test)
#
# clf.fit(X_train_scaler, y_train)
# predictions_scaler = clf.predict(X_test_scaler)
#
# accuracy_test_scaler = accuracy_score(y_test, predictions_scaler)
#
# print(accuracy_test_scaler)
#
# diff_scaler = accuracy_test_scaler - accuracy_test
# print(round(diff_scaler, 3))
# print(X_test_scaler)
# with open('result.txt', 'w', encoding='ansi') as f:
#     f.write(str(round(diff_scaler, 3)))
