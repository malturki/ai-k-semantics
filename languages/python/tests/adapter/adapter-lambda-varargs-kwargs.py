collect = lambda first, *rest, **kw: first == 1 and rest == (2, 3) and kw == {"bonus": 4, "extra": 5}
positional_only = lambda *items, **kw: items == (1, 2) and kw == {}
keyword_first = lambda first, *rest, **kw: first == 9 and rest == () and kw == {"x": 10}

result = collect(1, 2, 3, bonus=4, extra=5)
result = result and positional_only(1, 2)
result = result and keyword_first(first=9, x=10)
assert result
result
