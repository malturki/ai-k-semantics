seed = 2


def only(x=seed, /):
    return x == 2


def only_override(x=seed, /):
    return x == 5


def combined(x, y=seed, /, z=3, w=4):
    return x * 1000 + y * 100 + z * 10 + w


def rest_keywords(x=1, /, y=2, z=3):
    return x == 1 and y == 6 and z == 3


seed = 99
result = only()
result = result and only_override(5)
result = result and combined(1) == 1234
result = result and combined(1, 4) == 1434
result = result and combined(1, 4, 5) == 1454
result = result and combined(1, z=6, w=7) == 1267
result = result and combined(1, 4, w=8) == 1438
result = result and rest_keywords(y=6)
assert result
result
