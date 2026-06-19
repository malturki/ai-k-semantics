seed = 2

def collect(x, y=seed, *rest):
    return x * 100 + y * 10 + len(rest)

seed = 99
result = collect(1) == 120
result = result and collect(1, 3, 4) == 131
result = result and collect(1, 3, 4, 5) == 132
result = result and collect(x=1) == 120
result = result and collect(1, y=3) == 130
assert result
result
