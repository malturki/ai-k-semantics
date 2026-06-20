choose = lambda *, a, b=2, **kw: a == 1 and b == 2 and kw == {"bonus": 5}
sparse = lambda *, a=1, b, c=3, **kw: a == 1 and b == 4 and c == 3 and kw == {"tag": 6, "extra": 7}

result = choose(a=1, bonus=5)
result = result and choose(a=8, b=9, label=10) == False
result = result and sparse(b=4, tag=6, extra=7)
assert result
result
