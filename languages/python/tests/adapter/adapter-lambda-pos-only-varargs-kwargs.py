seed = 5

collect = lambda x, /, y, *args, **kw: x * 10000 + y * 1000 + len(args) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)
defaults = lambda x=seed, /, y=4, *args, **kw: x * 10000 + y * 1000 + len(args) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)

seed = 99

result = collect(1, 2) == 12000
result = result and collect(1, 2, 3, 4, x=5, z=6) == 12231
result = result and collect(1, y=2, x=5, z=6) == 12031
result = result and defaults(x=6) == 54016
result = result and defaults(7, 8, 9, x=5) == 78115
result = result and defaults(7, y=8, x=5, z=6) == 78031

assert result
result
