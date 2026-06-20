seed = 2


def required(x, *items, scale):
    return x == 1 and items == (2, 3) and scale == 4


def defaults(x=seed, *items, scale=2, offset, tag=3):
    return x == 2 and items == (5, 6) and scale == 2 and offset == 7 and tag == 3


def all_keywords(x, *items, scale, offset=1):
    return x == 8 and items == () and scale == 9 and offset == 1


def override(x=1, *items, scale=2, offset=3):
    return x == 4 and items == (5,) and scale == 6 and offset == 7


seed = 99
result = required(1, 2, 3, scale=4)
result = result and defaults(2, 5, 6, offset=7)
result = result and all_keywords(x=8, scale=9)
result = result and override(4, 5, scale=6, offset=7)
assert result
result
