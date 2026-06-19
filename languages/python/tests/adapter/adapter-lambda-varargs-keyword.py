collect = lambda x, y, *rest: x * 100 + y * 10 + len(rest)

result = collect(x=1, y=2) == 120
result = result and collect(1, y=2) == 120
result = result and collect(1, 2, 3, 4) == 122
assert result
result
