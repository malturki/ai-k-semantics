def combine(a, b, c=0):
    return a * 100 + b * 10 + c

make = lambda a, b, c=0: a * 100 + b * 10 + c

kw = {"b": 2, "c": 3}
result = combine(1, **kw) == 123
result = result and combine(4, c=6, **{"b": 5}) == 456
result = result and make(7, **{"b": 8, "c": 9}) == 789
assert result
result
