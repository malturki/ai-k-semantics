negate = lambda x: 0 - x
square = lambda x: x * x
first = lambda item: item[0]

result = min([3, 1, 2], key=negate) == 3
result = result and max([3, 1, 2], key=negate) == 1
result = result and min(3, 1, 2, key=negate) == 3
result = result and max(3, 1, 2, key=negate) == 1

result = result and min([2, -3, 1], key=square) == 1
result = result and max([2, -3, 1], key=square) == -3
result = result and min(range(1, 4), key=negate) == 3
result = result and max(range(1, 4), key=negate) == 1

items = [(1, 3), (1, 2), (2, 1)]
result = result and min(items, key=first) == (1, 3)
result = result and max(items, key=first) == (2, 1)
result = result and min((3, 1, 2), key=None) == 1
result = result and max({1: "a", 4: "b", 2: "c"}, key=None) == 4

min_empty_key_error = False
try:
    min([], key=negate)
except ValueError:
    min_empty_key_error = True

max_empty_key_error = False
try:
    max((), key=negate)
except ValueError:
    max_empty_key_error = True

result = result and min_empty_key_error and max_empty_key_error
assert result
result
