import codecs
import locale

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


with open("files/wine.data", "r") as file_01:
    data = file_01.read()

winedata = pd.read_csv("files/wine.data")
print(type(winedata))
print(winedata)
print('----------------')
print(winedata[0:0])

