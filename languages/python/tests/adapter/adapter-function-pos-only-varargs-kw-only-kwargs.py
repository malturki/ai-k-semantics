seed = 4

def collect(x, /, y, *args, z, **kw):
    return x * 1000000 + y * 100000 + z * 10000 + len(args) * 1000 + (args[0] if len(args) else 0) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

def defaults(x=seed, /, y=3, *args, z=5, w=7, **kw):
    return x * 1000000 + y * 100000 + z * 10000 + w * 1000 + len(args) * 100 + (args[0] if len(args) else 0) * 10 + len(kw) + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

seed = 99

result = collect(1, 2, z=3) == 1230000
result = result and collect(1, 2, 4, 5, z=3, q=6) == 1232416
result = result and collect(1, y=2, z=3, x=7, q=6) == 1230033
result = result and defaults(x=6, z=8) == 4387007
result = result and defaults(9, 8, 6, 5, z=4, w=1, q=2) == 9841263

assert result
result
