seed = 5

collect = lambda x, /, y, *, z, **kw: x * 100000 + y * 10000 + z * 1000 + len(kw) * 100 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)
defaults = lambda x=seed, /, y=4, *, z=6, w=8, **kw: x * 100000 + y * 10000 + z * 1000 + w * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)

seed = 99

result = collect(1, 2, z=3) == 123000
result = result and collect(1, 2, z=3, x=4, q=5) == 123209
result = result and collect(1, y=2, z=3, x=4) == 123104
result = result and defaults(x=7, z=9) == 549817
result = result and defaults(9, z=8, w=1, q=2) == 948112
result = result and defaults(9, y=8, z=6, x=5, q=4) == 986829

assert result
result
