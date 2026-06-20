seed = 5

collect = lambda x, /, y, **kw: x * 1000 + y * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)
defaults = lambda x=seed, /, y=4, **kw: x * 1000 + y * 100 + len(kw) * 10 + (kw["x"] if "x" in kw else 0) + (kw["z"] if "z" in kw else 0)

seed = 99

result = collect(1, 2) == 1200
result = result and collect(1, y=2, z=5) == 1215
result = result and collect(1, 2, x=7, z=5) == 1232
result = result and defaults() == 5400
result = result and defaults(x=7) == 5417
result = result and defaults(y=6, z=5) == 5615
result = result and defaults(5, y=6, x=7) == 5617
assert result
result
