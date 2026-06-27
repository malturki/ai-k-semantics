negate = lambda x: 0 - x
first = lambda item: item[0]
label = lambda x: "a" if x == 2 else "b"
same_key = lambda x: 0

result = sorted([3, 1, 2], key=negate) == [3, 2, 1]
result = result and sorted(range(1, 4), key=negate) == [3, 2, 1]
result = result and sorted([2, 1], key=label) == [2, 1]
result = result and sorted((3, 1, 2), key=None) == [1, 2, 3]
result = result and sorted([3, 1, 2], key=None, reverse=True) == [3, 2, 1]

items = [(1, 3), (1, 2), (0, 9)]
result = result and sorted(items, key=first) == [(0, 9), (1, 3), (1, 2)]
result = result and sorted(items, key=first, reverse=True) == [(1, 3), (1, 2), (0, 9)]
result = result and sorted(items, reverse=True, key=first) == [(1, 3), (1, 2), (0, 9)]

order = 0
result = result and sorted(
    [(order := order * 10 + 1), 2],
    key=(order := order * 10 + 2) and (lambda x: x),
    reverse=(order := order * 10 + 3) and [],
) == [1, 2]
result = result and order == 123

order = 0
result = result and sorted(
    [(order := order * 10 + 1), 2],
    reverse=(order := order * 10 + 3) and [],
    key=(order := order * 10 + 2) and (lambda x: x),
) == [1, 2]
result = result and order == 132

result = result and sorted(items, key=same_key) == items
result = result and sorted(items, key=same_key, reverse=True) == items
result = result and sorted([], key=3) == []

noncallable_key_error = False
try:
    sorted([1], key=3)
except TypeError:
    noncallable_key_error = True
result = result and noncallable_key_error

key_eval_error = False
try:
    sorted(3, key=1 // 0)
except ZeroDivisionError:
    key_eval_error = True
result = result and key_eval_error

reverse_eval_before_type_error = False
try:
    sorted(3, key=(lambda x: x), reverse=1 // 0)
except ZeroDivisionError:
    reverse_eval_before_type_error = True
result = result and reverse_eval_before_type_error

bad_key = lambda x: x

mixed_key_error = False
try:
    sorted([1, "x"], key=bad_key)
except TypeError:
    mixed_key_error = True
result = result and mixed_key_error

result
