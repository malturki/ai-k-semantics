def shape(first=1, second=2, *rest, **kw):
    return first == 1 and second == 2 and rest == () and kw == {"bonus": 5}


def mixed(first=1, second=2, *rest, **kw):
    return first == 3 and second == 4 and rest == (5, 6) and kw == {"bonus": 7, "extra": 8}


def keyword_fill(first=1, second=2, *rest, **kw):
    return first == 8 and second == 9 and rest == () and kw == {"bonus": 10}


result = shape(bonus=5)
result = result and mixed(3, 4, 5, 6, bonus=7, extra=8)
result = result and keyword_fill(8, second=9, bonus=10)
assert result
result
