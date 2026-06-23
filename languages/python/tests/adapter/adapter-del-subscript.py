xs = [1, 2, 3, 4]
del xs[1]
del xs[-1]

ys = [5, 6, 7]
del ys[True]

d = {"a": 1, "b": 2, "c": 3}
del d["b"]
del d["a"]

single = [9]
del single[0]

only = {"z": 9}
del only["z"]

result = xs == [1, 3] and ys == [5, 7] and d == {"c": 3} and single == [] and only == {}
assert result
result
