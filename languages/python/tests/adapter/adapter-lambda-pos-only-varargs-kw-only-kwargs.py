seed = 5

collect = lambda x, /, y, *args, z, **kw: x * 1000000 + y * 100000 + z * 10000 + len(args) * 1000 + (args[0] if len(args) else 0) * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)
defaults = lambda x=seed, /, y=4, *args, z=6, w=8, **kw: x * 1000000 + y * 100000 + z * 10000 + w * 1000 + len(args) * 100 + (args[0] if len(args) else 0) * 10 + len(kw) + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

seed = 99

result = collect(1, 2, z=3) == 1230000
result = result and collect(1, 2, 4, 5, z=3, q=6) == 1232416
result = result and collect(1, y=2, z=3, x=7, q=6) == 1230033
result = result and defaults(x=7, z=9) == 5498008
result = result and defaults(9, 8, 6, 5, z=4, w=1, q=2) == 9841263

assert result
result
