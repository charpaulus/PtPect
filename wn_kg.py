#def f(x, y):
#    if x > y:
#        return 0
#    if x == y:
#        return 1
#    return f(x + 2, y) + f(x * 3, y) + f(x * 4, y)
#
#print(f(1, 11))

def f(x, y, x1, x2, x3, k):
    x3 = x2; x2 = x1; x1 = x
    if x1 * x2 * x3 != 0 and (x1 + x2 + x3) % 11 == 0: k += 1
    if x == y and k > 0: return 1
    if x > y: return 0
    return f(x+2,y,x1,x2,x3,k) + f(x*3,y,x1,x2,x3,k) + f(x*4,y,x1,x2,x3,k)

print(f(1, 600, 0, 0, 0, 0))