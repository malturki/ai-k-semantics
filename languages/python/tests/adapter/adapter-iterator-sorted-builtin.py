result = True

sorted_it = iter([3, 1, 2])
result = result and sorted(sorted_it) == [1, 2, 3]
result = result and next(sorted_it, "done") == "done"

reverse_it = iter([3, 1, 2])
result = result and sorted(reverse_it, reverse=True) == [3, 2, 1]
result = result and next(reverse_it, 7) == 7

negate = lambda x: 0 - x
same_key = lambda x: 0

key_it = iter([1, 2, 3])
result = result and sorted(key_it, key=negate) == [3, 2, 1]
result = result and next(key_it, 8) == 8

key_none_it = iter([2, 1, 3])
result = result and sorted(key_none_it, key=None) == [1, 2, 3]
result = result and next(key_none_it, 9) == 9

key_reverse_it = iter([1, 2, 3])
result = result and sorted(key_reverse_it, key=negate, reverse=True) == [1, 2, 3]
result = result and next(key_reverse_it, 10) == 10

reverse_key_it = iter([1, 2, 3])
result = result and sorted(reverse_key_it, reverse=True, key=negate) == [1, 2, 3]
result = result and next(reverse_key_it, 11) == 11

stable_it = iter([3, 1, 2])
result = result and sorted(stable_it, key=same_key, reverse=True) == [3, 1, 2]
result = result and next(stable_it, 12) == 12

empty_key_it = iter([])
result = result and sorted(empty_key_it, key=3) == []
result = result and next(empty_key_it, 13) == 13

bad_key_it = iter([1])
bad_key_error = False
try:
    sorted(bad_key_it, key=3)
except TypeError:
    bad_key_error = True
result = result and bad_key_error
result = result and next(bad_key_it, 14) == 14

source_sorted = iter([3, 1, 2, 99])


def pull_sorted():
    return next(source_sorted)


callable_sorted = iter(pull_sorted, 99)
result = result and sorted(callable_sorted) == [1, 2, 3]
result = result and next(callable_sorted, 15) == 15

source_key = iter([1, 3, 2, 99])


def pull_key():
    return next(source_key)


callable_key = iter(pull_key, 99)
result = result and sorted(callable_key, key=negate) == [3, 2, 1]
result = result and next(callable_key, 16) == 16

assert result
result
