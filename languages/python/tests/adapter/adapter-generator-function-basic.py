result = True


def simple():
    yield 1
    yield 2
    yield 3


result = result and callable(simple)

g = simple()
result = result and next(g) == 1
result = result and list(g) == [2, 3]
result = result and next(g, "done") == "done"

result = result and list(simple()) == [1, 2, 3]
result = result and tuple(simple()) == (1, 2, 3)


def add_pair(x, y):
    yield x
    yield x + y
    yield y


h = add_pair(4, 5)
result = result and tuple(h) == (4, 9, 5)
result = result and list(add_pair(1, 2)) == [1, 3, 2]

total = 0
for value in simple():
    total = total + value
result = result and total == 6


def yields_none():
    yield
    yield 7


n = yields_none()
result = result and next(n) is None
result = result and list(n) == [7]

assert result
result
