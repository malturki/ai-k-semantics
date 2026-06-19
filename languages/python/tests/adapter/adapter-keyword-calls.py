def ident(x):
    return x

result = ident(x=9) == 9

def blend(a, b=2, c=3):
    return a * 100 + b * 10 + c

result = result and blend(a=1, b=2, c=4) == 124
result = result and blend(c=7, a=5, b=6) == 567
result = result and blend(a=4) == 423
result = result and blend(c=6, a=4) == 426

f = lambda x, y=2: x * 10 + y
result = result and f(x=3) == 32
result = result and f(y=8, x=7) == 78

marker = 0

def pack(a, b, c):
    return a * 100 + b * 10 + c

result = result and pack(c=(marker := marker + 1), a=(marker := marker + 1), b=(marker := marker + 1)) == 231
result = result and marker == 3

def empty_default(x=1):
    pass

result = result and empty_default(x=2) is None
assert result
result
