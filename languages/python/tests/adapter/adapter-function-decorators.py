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
def target():
    return 0


result = target() == 1
result = result and second(target)() == 2

selected = first


@(selected := first)
@(selected := second)
def chosen():
    return 0


result = result and chosen() == 1
result = result and selected(chosen)() == 2
result
