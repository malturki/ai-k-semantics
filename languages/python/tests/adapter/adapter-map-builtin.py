def inc(x):
    return x + 1


def add(x, y):
    return x + y


def pair(x, y):
    return (x, y)


result = list(map(inc, [1, 2, 3])) == [2, 3, 4]
result = result and tuple(map(lambda x: x * 2, (2, 3))) == (4, 6)
result = result and list(map(add, [1, 2], [10, 20, 30])) == [11, 22]
result = result and list(map(pair, "ab", [1, 2])) == [("a", 1), ("b", 2)]
result = result and list(map(lambda b: b + 1, b"\x01\x02")) == [2, 3]
result = result and list(map(lambda x: x * 2, range(2, 5))) == [4, 6, 8]
result = result and list(map(lambda k: k + 1, {1: "a", 2: "b"})) == [2, 3]
result = result and bool(map(inc, [])) == True

total = 0
for value in map(inc, [1, 2]):
    total += value
result = result and total == 5

pairs_total = 0
for a, b in map(pair, [1, 2], [3, 4]):
    pairs_total += a * b
result = result and pairs_total == 11

marker = 0
for value in map(inc, []):
    marker = 99
else:
    marker = 7
result = result and marker == 7

result = result and list(map(add, [1, 2], [10, 20], strict=True)) == [11, 22]
result = result and list(map(add, [1, 2], [10], strict=False)) == [11]

strict_error = False
try:
    list(map(add, [1, 2], [10], strict=True))
except ValueError:
    strict_error = True

bad_iterable = False
try:
    map(inc, 1)
except TypeError:
    bad_iterable = True

bad_arity = False
try:
    map(inc)
except TypeError:
    bad_arity = True

bad_callable = False
try:
    list(map(1, [2]))
except TypeError:
    bad_callable = True

result = result and strict_error and bad_iterable and bad_arity and bad_callable
assert result
result
