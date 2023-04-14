import zipfile
import json

with zipfile.ZipFile('input.zip') as fzip:
    c = 0
    for el in fzip.infolist():
        if el.external_attr == 32:
            fl = el.filename.split('.')
            if fl[len(fl) - 1] == 'json':
                with fzip.open(el.filename) as fjs:
                    data = json.load(fjs)
                    if data['city'] == 'Москва':
                        c += 1
    print(c)
