xs = [10, 20, 30]
i = 0
xs[(i := 1)] += (i := 5)
xs[-1] *= 2
xs[False] += xs[1]

d = {"a": 2, "b": 7}
key = "a"
d[key] **= 3
d["b"] //= 2

result = xs == [35, 25, 60] and i == 5 and d == {"a": 8, "b": 3}
assert result
result
