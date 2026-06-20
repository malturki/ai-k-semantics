seed = 4

def collect(x, /, y, *args, **kw):
    return x * 10000 + y * 1000 + len(args) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)

def defaults(x=seed, /, y=3, *args, **kw):
    return x * 10000 + y * 1000 + len(args) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)

seed = 99

result = collect(1, 2) == 12000
result = result and collect(1, 2, 3, 4, x=5, z=6) == 12231
result = result and collect(1, y=2, x=5, z=6) == 12031
result = result and defaults(x=5) == 43015
result = result and defaults(7, 8, 9, x=5) == 78115
result = result and defaults(7, y=8, x=5, z=6) == 78031

assert result
result
