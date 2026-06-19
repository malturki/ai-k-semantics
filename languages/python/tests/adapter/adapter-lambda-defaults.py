seed = 3
f = lambda x=seed + 2: x
seed = 99
result = f() == 5
result = result and f(7) == 7

g = lambda a, b=2, c=3: a * 100 + b * 10 + c
result = result and g(4) == 423
result = result and g(4, 5) == 453
result = result and g(4, 5, 6) == 456

base = 1
h = lambda x=(base := base + 1), y=(base := base + 1): x * 10 + y
result = result and base == 3
result = result and h() == 23
result = result and h(8) == 83

empty = lambda x=1: None
result = result and empty() is None
assert result
result
