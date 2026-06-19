def collect(x, **kw):
    return x * 100 + len(kw) * 10 + kw["bonus"]

def just(**kw):
    return len(kw) + kw["x"]

result = collect(1, bonus=5) == 115
result = result and collect(x=2, bonus=7, extra=3) == 227
result = result and collect(3, bonus=4, extra=8) == 324
result = result and just(x=4) == 5
assert result
result
