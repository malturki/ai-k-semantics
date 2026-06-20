seed = 2

required = lambda x, *items, scale, **kw: x == 1 and items == (2, 3) and scale == 4 and kw == {"tag": 5}
defaults = lambda x=seed, *items, scale=2, offset, tag=3, **kw: x == 2 and items == (5, 6) and scale == 2 and offset == 7 and tag == 3 and kw == {"extra": 8}
all_keywords = lambda x, *items, scale, offset=1, **kw: x == 8 and items == () and scale == 9 and offset == 1 and kw == {"more": 10}
override = lambda x=1, *items, scale=2, offset=3, **kw: x == 4 and items == (5,) and scale == 6 and offset == 7 and kw == {"other": 11}

seed = 99
result = required(1, 2, 3, scale=4, tag=5)
result = result and defaults(2, 5, 6, offset=7, extra=8)
result = result and all_keywords(x=8, scale=9, more=10)
result = result and override(4, 5, scale=6, offset=7, other=11)
assert result
result
