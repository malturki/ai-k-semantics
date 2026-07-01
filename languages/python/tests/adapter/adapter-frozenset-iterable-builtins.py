truth_ok = all(frozenset([1, True, "x"]))
truth_ok = truth_ok and not all(frozenset([0, 1]))
truth_ok = truth_ok and all(frozenset())
truth_ok = truth_ok and any(frozenset([0, 2]))
truth_ok = truth_ok and not any(frozenset([0]))
truth_ok = truth_ok and not any(frozenset())

sum_ok = sum(frozenset([1, 2, 3])) == 6
sum_ok = sum_ok and sum(frozenset(), 7) == 7
sum_ok = sum_ok and sum(frozenset([1, 2]), 10) == 13

sum_start_error = False
try:
    sum(frozenset(), "")
except TypeError:
    sum_start_error = True

sum_item_error = False
try:
    sum(frozenset(["x"]))
except TypeError:
    sum_item_error = True

minmax_ok = min(frozenset([3, 1, 2])) == 1
minmax_ok = minmax_ok and max(frozenset([3, 1, 2])) == 3
minmax_ok = minmax_ok and min(frozenset(), default=99) == 99
minmax_ok = minmax_ok and max(frozenset(), default=-1) == -1
minmax_ok = minmax_ok and min(frozenset([3, 1, 2]), default=99) == 1
minmax_ok = minmax_ok and max(frozenset([3, 1, 2]), default=-1) == 3

negate = lambda x: 0 - x
key_ok = min(frozenset([3, 1, 2]), key=negate) == 3
key_ok = key_ok and max(frozenset([3, 1, 2]), key=negate) == 1
key_ok = key_ok and min(frozenset([3, 1, 2]), default=99, key=negate) == 3
key_ok = key_ok and max(frozenset([3, 1, 2]), key=negate, default=-1) == 1
key_ok = key_ok and min(frozenset([3, 1, 2]), key=None) == 1
key_ok = key_ok and max(frozenset([3, 1, 2]), key=None, default=-1) == 3
key_ok = key_ok and min(frozenset(), default=99, key=negate) == 99
key_ok = key_ok and max(frozenset(), key=negate, default=-1) == -1

min_empty_error = False
try:
    min(frozenset())
except ValueError:
    min_empty_error = True

max_empty_error = False
try:
    max(frozenset())
except ValueError:
    max_empty_error = True

result = truth_ok and sum_ok and sum_start_error and sum_item_error
result = result and minmax_ok and key_ok and min_empty_error and max_empty_error

assert result
result
