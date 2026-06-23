xs = [0, 1, 2, 3, 4]
xs[1:4] = [10, 11]
xs[:1] = (7, 8)
xs[3:3] = [9]
xs[-2:] = []
del xs[1:3]
del xs[1:1]

ys = [1, 2]
ys[5:10] = [3]

zs = [1, 2]
zs[:] = []

result = xs == [7, 9] and ys == [1, 2, 3] and zs == []
assert result
result
