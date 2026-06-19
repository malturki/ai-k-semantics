def ident(x):
    return x

result = ident(9) == 9

def blend(a, b=2, c=3):
    return a * 100 + b * 10 + c

result = result and blend(1, c=4) == 124
result = result and blend(1, b=6, c=7) == 167
result = result and blend(5, 6, c=7) == 567
result = result and blend(4, c=6) == 426

f = lambda x, y=2, z=3: x * 100 + y * 10 + z
result = result and f(3, z=5) == 325
result = result and f(7, y=8) == 783

marker = 0

def pack(a, b, c):
    return a * 100 + b * 10 + c

result = result and pack((marker := marker + 1), c=(marker := marker + 1), b=(marker := marker + 1)) == 132
result = result and marker == 3

def empty_default(x=1, y=2):
    pass

result = result and empty_default(9, y=8) is None
assert result
result
