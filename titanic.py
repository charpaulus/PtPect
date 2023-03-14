import pandas as pd


def first_name(rws):
    s = rws.Name.split()
    res = 0
    lf_bkt = 0
    for i in range(len(s)):
        s[i] = s[i].strip('.,')
        if s[i] == 'Miss':
            res = s[i+1]
        elif s[i] == 'Mme':
            res = s[i+1]
        elif s[i] == 'Mlle':
            res = s[i+1]
        elif s[i] == 'Ms':
            res = s[i+1]
        elif s[i] == 'Dr':
            res = s[i+1]
        elif s[i] == 'Lady':
            res = s[i+1]
        elif s[i] == 'Countess':
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


data = pd.read_csv('titanic.csv', index_col='PassengerId')
f = open('titanic-week1.txt', 'w')
data_sex = data.loc[data.Sex == 'female']
data_sex.loc[:, 'first_name'] = data_sex.apply(first_name, axis=1)
print(data_sex.first_name.describe().top, file=f)
print('Check with 2 file')
