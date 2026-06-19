seed = 2
collect = lambda x, y=seed, *rest: x * 100 + y * 10 + len(rest)

seed = 99
result = collect(1) == 120
result = result and collect(1, 3, 4) == 131
result = result and collect(1, 3, 4, 5) == 132
result = result and collect(x=1) == 120
result = result and collect(1, y=3) == 130
assert result
result
