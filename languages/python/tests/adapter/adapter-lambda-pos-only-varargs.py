seed = 3

collect = lambda x, /, y, *rest: x * 1000 + y * 100 + len(rest) * 10 + (rest[0] if rest else 0)
defaults = lambda x=seed, /, y=4, *rest: x * 1000 + y * 100 + len(rest) * 10 + (rest[0] if rest else 0)

seed = 99

result = collect(1, 2) == 1200
result = result and collect(1, 2, 7, 8) == 1227
result = result and collect(1, y=4) == 1400
result = result and defaults() == 3400
result = result and defaults(5) == 5400
result = result and defaults(y=6) == 3600
result = result and defaults(5, 6, 7) == 5617
result = result and defaults(5, y=6) == 5600
assert result
result
