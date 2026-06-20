seed = 2


def collect(x, /, y, *rest):
    return x * 1000 + y * 100 + len(rest) * 10 + (rest[0] if rest else 0)


def defaults(x=seed, /, y=3, *rest):
    return x * 1000 + y * 100 + len(rest) * 10 + (rest[0] if rest else 0)


seed = 99

result = collect(1, 2) == 1200
result = result and collect(1, 2, 7, 8) == 1227
result = result and collect(1, y=4) == 1400
result = result and defaults() == 2300
result = result and defaults(5) == 5300
result = result and defaults(y=6) == 2600
result = result and defaults(5, 6, 7) == 5617
result = result and defaults(5, y=6) == 5600
assert result
result
