import zipfile

def human_read_format(size):
    k = 0
    pristavka = ['Б', 'КБ', 'МБ', 'ГБ']
    while size >= 1024 and k < 4:
        k += 1
        size = size / 1024
    return f'{round(size)}{pristavka[k]}'

with zipfile.ZipFile('files/input.zip') as fzip:
    for el01 in fzip.infolist():
        way = el01.filename.rstrip('/').split('/')
        if el01.external_attr == 16:
            print('  ' * (len(way) - 1) + way[-1])
        else:
            print('  ' * (len(way) - 1) + way[-1], ' ', human_read_format(el01.file_size), sep='')
