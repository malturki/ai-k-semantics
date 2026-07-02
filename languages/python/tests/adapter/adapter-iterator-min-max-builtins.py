result = True

min_it = iter([3, 1, 2])
result = result and min(min_it) == 1
result = result and next(min_it, "done") == "done"

max_it = iter([3, 1, 2])
result = result and max(max_it) == 3
result = result and next(max_it, "done") == "done"

empty_min = iter([])
empty_min_error = False
try:
    min(empty_min)
except ValueError:
    empty_min_error = True
result = result and empty_min_error
result = result and next(empty_min, 7) == 7

empty_max = iter([])
empty_max_error = False
try:
    max(empty_max)
except ValueError:
    empty_max_error = True
result = result and empty_max_error
result = result and next(empty_max, 8) == 8

min_default_it = iter([])
result = result and min(min_default_it, default=9) == 9
result = result and next(min_default_it, 10) == 10

max_default_it = iter([1, 4, 2])
result = result and max(max_default_it, default=0) == 4
result = result and next(max_default_it, 11) == 11

negate = lambda x: 0 - x
same_key = lambda x: 0

min_key_it = iter([1, 2, 3])
result = result and min(min_key_it, key=negate) == 3
result = result and next(min_key_it, 12) == 12

max_key_it = iter([1, 2, 3])
result = result and max(max_key_it, key=negate) == 1
result = result and next(max_key_it, 13) == 13

min_key_none_it = iter([4, 2, 5])
result = result and min(min_key_none_it, key=None) == 2
result = result and next(min_key_none_it, 14) == 14

max_key_default_it = iter([1, 2])
result = result and max(max_key_default_it, key=negate, default=0) == 1
result = result and next(max_key_default_it, 15) == 15

min_default_key_it = iter([])
result = result and min(min_default_key_it, default=16, key=negate) == 16
result = result and next(min_default_key_it, 17) == 17

tie_it = iter([5, 4])
result = result and min(tie_it, key=same_key) == 5
result = result and next(tie_it, 18) == 18

source_min = iter([5, 2, 4, 99])


def pull_min():
    return next(source_min)


callable_min = iter(pull_min, 99)
result = result and min(callable_min) == 2
result = result and next(callable_min, 19) == 19

source_max_key = iter([1, 3, 2, 99])


def pull_max_key():
    return next(source_max_key)


callable_max_key = iter(pull_max_key, 99)
result = result and max(callable_max_key, key=negate) == 1
result = result and next(callable_max_key, 20) == 20

source_empty = iter([99])


def pull_empty():
    return next(source_empty)


callable_empty = iter(pull_empty, 99)
result = result and min(callable_empty, default=21) == 21
result = result and next(callable_empty, 22) == 22

assert result
result
