import zipfile
import json

with zipfile.ZipFile('input.zip') as fzip:
    print(fzip.infolist())
    k = 0
    for el in fzip.infolist():
        if el.external_attr == 32:
            fl = el.filename.split('.')
            if fl[len(fl)-1] == 'json':
                k += 1
    print(k)