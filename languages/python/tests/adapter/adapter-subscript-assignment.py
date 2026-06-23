xs = [1, 2, 3]
xs[0] = 4
xs[-1] = xs[0] + 5
xs[True] = 8

d = {"a": 1}
d["b"] = xs[2]
d["a"] = xs[0]

result = xs == [4, 8, 9] and d == {"a": 4, "b": 9}
assert result
result
