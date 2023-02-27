import functools

myLine = []
for ln in list(open('input.txt').readlines()):
    myLine += ln.split()
print(len(set(myLine)))

print(len(set(functools.reduce(lambda x, y: x+y, map(lambda x: x.split(), open('input.txt').readlines())))))

import functools
print(list(open('input.txt').readlines()))
print(list(map(lambda x: x.split(), open('input.txt').readlines())))
print(len(set(functools.reduce(lambda x, y: x+y, map(lambda x: x.split(), open('input.txt').readlines())))))
print(functools.reduce(lambda myLine, ln: myLine + len(ln.split()), list(open('input.txt').readlines()), 0))
