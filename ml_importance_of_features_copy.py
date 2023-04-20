import pandas as pd


def first_name(rws):
    s = rws.Name.split()
    res = 0
    lf_bkt = 0
    list_temp = ['Miss', 'Mme', 'Mlle', 'Ms', 'Dr', 'Lady', 'Countess']
    for i in range(len(s)):
        s[i] = s[i].strip('.,')
        if s[i] in list_temp:
            res = s[i+1]
        elif s[i] == 'Mrs':
            for j in range(i+1, len(s)):
                for k in s[j]:
                    if k == '(':
                        lf_bkt = 1
                        res = s[j].strip('()')
            if lf_bkt == 0:
                res = s[i+1]
    return res


data = pd.read_csv('files/titanic.csv', index_col='PassengerId')
f = open('files/titanic-week1.txt', 'w')
data_sex = data.loc[data.Sex == 'female']
data_sex.loc[:, 'first_name'] = data_sex.apply(first_name, axis=1)
print(data_sex.first_name.describe().top, file=f)
