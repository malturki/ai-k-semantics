def required(x, *, scale, **kw):
    return x == 3 and scale == 4 and kw == {"tag": 5}


def suffix(x, y=2, *, scale, offset=1, **kw):
    return x == 3 and y == 2 and scale == 4 and offset == 1 and kw == {"tag": 5}


def all_given(x, y=2, *, scale, offset=1, **kw):
    return x == 3 and y == 4 and scale == 5 and offset == 6 and kw == {"extra": 7}


def by_keyword(x, y=2, *, scale, offset=1, **kw):
    return x == 8 and y == 2 and scale == 9 and offset == 1 and kw == {"more": 10}


def sparse(x=1, *, a=2, b, c=3, **kw):
    return x == 1 and a == 2 and b == 4 and c == 3 and kw == {"tag": 6}


result = required(3, scale=4, tag=5)
result = result and required(x=3, scale=4, tag=5)
result = result and suffix(3, scale=4, tag=5)
result = result and all_given(3, 4, scale=5, offset=6, extra=7)
result = result and by_keyword(x=8, scale=9, more=10)
result = result and sparse(b=4, tag=6)
assert result
result
