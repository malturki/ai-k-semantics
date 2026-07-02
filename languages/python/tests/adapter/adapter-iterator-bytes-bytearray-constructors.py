result = True

bytes_it = iter([65, 66, 67])
result = result and bytes(bytes_it) == b"ABC"
result = result and next(bytes_it, 9) == 9

empty_bytes_it = iter([])
result = result and bytes(empty_bytes_it) == b""
result = result and next(empty_bytes_it, 10) == 10

bytearray_it = iter([1, 2, 3])
ba = bytearray(bytearray_it)
result = result and ba == bytearray([1, 2, 3])
result = result and next(bytearray_it, 11) == 11

empty_bytearray_it = iter([])
result = result and bytearray(empty_bytearray_it) == bytearray()
result = result and next(empty_bytearray_it, 12) == 12

source_bytes = iter([65, 66, 99])


def pull_bytes():
    return next(source_bytes)


callable_bytes = iter(pull_bytes, 99)
result = result and bytes(callable_bytes) == b"AB"
result = result and next(callable_bytes, 13) == 13

source_bytearray = iter([4, 5, 99])


def pull_bytearray():
    return next(source_bytearray)


callable_bytearray = iter(pull_bytearray, 99)
result = result and bytearray(callable_bytearray) == bytearray([4, 5])
result = result and next(callable_bytearray, 14) == 14

bad_type = iter([1, "x", 2])
bad_type_seen = False
try:
    bytes(bad_type)
except TypeError:
    bad_type_seen = True

bad_value = iter([1, 256])
bad_value_seen = False
try:
    bytes(bad_value)
except ValueError:
    bad_value_seen = True

bad_array_type = iter([1, "x", 2])
bad_array_type_seen = False
try:
    bytearray(bad_array_type)
except TypeError:
    bad_array_type_seen = True

bad_array_value = iter([-1])
bad_array_value_seen = False
try:
    bytearray(bad_array_value)
except ValueError:
    bad_array_value_seen = True

result = (
    result
    and bad_type_seen
    and bad_value_seen
    and bad_array_type_seen
    and bad_array_value_seen
)

assert result
result
