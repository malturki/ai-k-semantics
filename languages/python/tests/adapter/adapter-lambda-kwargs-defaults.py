collect = lambda x=1, **kw: x * 100 + len(kw) * 10 + kw["bonus"]
pair = lambda x=2, y=3, **kw: x * 100 + y * 10 + len(kw) + kw["z"]

result = collect(bonus=5) == 115
result = result and collect(2, bonus=7, extra=3) == 227
result = result and collect(x=3, bonus=4) == 314
result = result and pair(y=4, z=5) == 246
assert result
result
