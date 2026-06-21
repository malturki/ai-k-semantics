order = 0


def identity(func):
    return func


@(order := order * 10 + 1) and identity
def target(x=(order := order * 10 + 2)):
    return x


result = target() == 12 and order == 12


def one():
    return 1


def two():
    return 2


def first(func):
    return one


def second(func):
    return two


@first
@second
def replaced(x=99):
    return x


result = result and replaced() == 1
result
