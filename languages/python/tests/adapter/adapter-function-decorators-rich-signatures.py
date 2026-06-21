order = 0
seed = 4


def identity(func):
    return func


@((order := order * 10 + 1) and identity)
def ordered(x=(order := order * 10 + 2), *items, scale=(order := order * 10 + 3), **kw):
    return x == 12 and items == (4, 5) and scale == 123 and kw == {"tag": 6}


@identity
def rich(x=seed, /, y=3, *args, z=5, w=7, **kw):
    return x * 1000000 + y * 100000 + z * 10000 + w * 1000 + len(args) * 100 + (args[0] if len(args) else 0) * 10 + len(kw) + (kw["x"] if "x" in kw else 0) + (kw["q"] if "q" in kw else 0)


@identity
def no_defaults(x, /, y, *args, z, **kw):
    return x == 1 and y == 2 and args == (3,) and z == 4 and kw == {"q": 5}


@identity
def only_kw(*, required, default=8, **extra):
    return required == 7 and default == 8 and extra == {"tag": 9}


seed = 99

result = order == 123 and ordered(12, 4, 5, tag=6)
result = result and rich(x=6, z=8) == 4387007
result = result and rich(9, 8, 6, 5, z=4, w=1, q=2) == 9841263
result = result and no_defaults(1, 2, 3, z=4, q=5)
result = result and only_kw(required=7, tag=9)
assert result
result
