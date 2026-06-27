result = sorted([]) == []
result = result and sorted([3, 1, 2]) == [1, 2, 3]
result = result and sorted((3, 1, 2)) == [1, 2, 3]
result = result and sorted("cab") == ["a", "b", "c"]
result = result and sorted(b"\x02\x00\x01") == [0, 1, 2]
result = result and sorted(range(5, 0, -2)) == [1, 3, 5]
result = result and sorted({"b": 1, "a": 2}) == ["a", "b"]
result = result and sorted([1.5, -2.0, 0.0]) == [-2.0, 0.0, 1.5]

non_iterable_type_error = False
try:
    sorted(3)
except TypeError:
    non_iterable_type_error = True
result = result and non_iterable_type_error

mixed_type_error = False
try:
    sorted([1, "x"])
except TypeError:
    mixed_type_error = True
result = result and mixed_type_error

result
