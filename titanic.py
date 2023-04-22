import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from graphviz import render
import os

os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
#import matplotlib.pyplot

file_tree = open('file_tree.txt', 'wb')
file_tree_02 = open('file_tree_02.txt', 'wb')
file_tit = open('file_tit.txt', "wb")
data_full = pd.read_csv('files/titanic.csv')
print(data_full)
print(data_full.columns.values)
data_filtered = pd.read_csv('files/titanic.csv', usecols=['Pclass', 'Age', 'Sex', 'Fare', 'Survived']).dropna().reset_index().replace('male', 1).replace('female', 0)
data_filtered_02 = pd.read_csv('files/titanic.csv', usecols=['Pclass', 'Age', 'Sex', 'Fare', 'Survived']).dropna().reset_index().replace('male', 0).replace('female', 1)
data = data_filtered[['Pclass', 'Age', 'Sex', 'Fare']]
data_csv = data.to_csv('file_tit.csv', columns=['Pclass', 'Age', 'Sex', 'Fare'])
#write_data_to_excel = pd.ExcelWriter('data.xlsx')
data.to_excel('data.xlsx')
data_02 = data_filtered_02[['Pclass', 'Age', 'Sex', 'Fare']]
data_02.to_excel('data_02.xlsx')
target_variable = data_filtered[['Survived']]
X = data
X_02 = data_02
X_03 = np.array(data)
Y = target_variable
clf = DecisionTreeClassifier(random_state=241)
clf_02 = DecisionTreeClassifier(random_state=241)
clf_03 = DecisionTreeClassifier()
clf.fit(X, Y)
clf_02.fit(X_02, Y)
clf_03.fit(X_03, Y)


importances = clf.feature_importances_
importances_02 = clf_02.feature_importances_
importances_03 = clf_03.feature_importances_
#print(data.sort_values(by=['Fare']).to_string())
#print(target_variable)
print(data.columns.values)
print('!!!!!!!!!!!!!!!!!!!!!!!!!')
print(importances)
print('02!!!!!!!!02')
print(importances_02)
print('03!!!!!!!!03')
print(importances_03)
r = tree.export_text(clf)
r_02 = tree.export_text(clf_02)
#print(r)

pickle.dump(r, file_tree)
pickle.dump(r_02, file_tree_02)
file_tree.close()
file_tree_02.close()
#pickle.dump(data.columns.values, file_tit)
#tree.plot_tree(clf)
#matplotlib.pyplot.show()
tree.export_graphviz(clf, out_file="tree.dot")
#render('dot', 'png', 'tree.dot')
os.system('dot -Tpng tree.dot -o tree.png')
