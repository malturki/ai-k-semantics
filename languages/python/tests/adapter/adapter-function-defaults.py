seed = 10

def add(x, y=seed + 1):
    return x + y

seed = 100
result = add(5) == 16
result = result and add(5, 7) == 12

def choose(a=1, b=2, c=3):
    return a * 100 + b * 10 + c

result = result and choose() == 123
result = result and choose(4) == 423
result = result and choose(4, 5) == 453
result = result and choose(4, 5, 6) == 456

base = 1

def pair(x=(base := base + 1), y=(base := base + 1)):
    return x * 10 + y

result = result and base == 3
result = result and pair() == 23
result = result and pair(8) == 83

def empty_default(x=1):
    pass

result = result and empty_default() is None
assert result
result
