seed = 4

def collect(x, /, y, *, z, **kw):
    return x * 100000 + y * 10000 + z * 1000 + len(kw) * 100 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

def defaults(x=seed, /, y=3, *, z=5, w=7, **kw):
    return x * 100000 + y * 10000 + z * 1000 + w * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

seed = 99

result = collect(1, 2, z=3) == 123000
result = result and collect(1, 2, z=3, x=4, q=5) == 123209
result = result and collect(1, y=2, z=3, x=4) == 123104
result = result and defaults(x=6, z=8) == 438716
result = result and defaults(9, z=8, w=1, q=2) == 938112
result = result and defaults(9, y=8, z=6, x=5, q=4) == 986729

assert result
result
