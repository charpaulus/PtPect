import pandas as pd

data_tit = pd.read_csv('files/titanic.csv', index_col='PassengerId')
data_work = data_tit[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']].dropna().drop('Survived', axis=1)
#tmp = data_work.dropna().drop('Survived', axis=1)
#tmp = tmp.drop('Survived', axis=1)
#print(data_tit['Survived'])
print(data_work.info())
#print(tmp.info())
#print(tmp1.info())

