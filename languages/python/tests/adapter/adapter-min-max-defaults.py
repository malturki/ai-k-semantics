result = min([], default=7) == 7
result = result and max((), default=-1) == -1
result = result and min("", default=4) == 4
result = result and max(b"", default=5) == 5
result = result and min({}, default=None) is None
result = result and max(set(), default=8) == 8
result = result and min(range(0), default=9) == 9
result = result and max(range(5, 5), default=10) == 10

result = result and min([3, 1, 2], default=99) == 1
result = result and max((True, False, 3), default=-1) == 3
result = result and min({3, 1, 2}, default=99) == 1
result = result and max({1: "a", 4: "b", 2: "c"}, default=-1) == 4
result = result and min(range(5, -1, -2), default=99) == 1
result = result and max(range(5, -1, -2), default=-1) == 5

min_empty_error = False
try:
    min([])
except ValueError:
    min_empty_error = True

max_empty_error = False
try:
    max(())
except ValueError:
    max_empty_error = True

min_empty_range_error = False
try:
    min(range(0))
except ValueError:
    min_empty_range_error = True

min_args_default_error = False
try:
    min(1, 2, default=0)
except TypeError:
    min_args_default_error = True

max_args_default_error = False
try:
    max(1, 2, default=0)
except TypeError:
    max_args_default_error = True

result = (
    result
    and min_empty_error
    and max_empty_error
    and min_empty_range_error
    and min_args_default_error
    and max_args_default_error
)
assert result
result
