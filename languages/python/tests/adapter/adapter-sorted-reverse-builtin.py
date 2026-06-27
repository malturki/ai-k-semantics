result = sorted([3, 1, 2], reverse=True) == [3, 2, 1]
result = result and sorted((3, 1, 2), reverse=False) == [1, 2, 3]
result = result and sorted("cab", reverse=1) == ["c", "b", "a"]
result = result and sorted(range(5, 0, -2), reverse=[]) == [1, 3, 5]

reverse_eval_error = False
try:
    sorted([1, 2], reverse=1 // 0)
except ZeroDivisionError:
    reverse_eval_error = True
result = result and reverse_eval_error

non_iterable_after_reverse_eval = False
try:
    sorted(3, reverse=1 // 0)
except ZeroDivisionError:
    non_iterable_after_reverse_eval = True
result = result and non_iterable_after_reverse_eval

mixed_type_error = False
try:
    sorted([1, "x"], reverse=True)
except TypeError:
    mixed_type_error = True
result = result and mixed_type_error

result
