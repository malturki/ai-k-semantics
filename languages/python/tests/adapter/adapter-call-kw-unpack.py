def pair(a, b):
    return a * 10 + b

make = lambda a, b: a * 10 + b

kw = {"b": 2}
result = pair(a=1, **kw) == 12
result = result and pair(**{"a": 3, "b": 4}) == 34
result = result and pair(**{"a": 5}, b=6) == 56
result = result and make(**{"a": 7, "b": 8}) == 78
assert result
result
