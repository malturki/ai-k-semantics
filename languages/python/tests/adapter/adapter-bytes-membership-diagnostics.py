result = True

result = result and 97 in b"abc"
result = result and 200 not in b"abc"
result = result and b"" in b"abc"
result = result and b"ab" in b"abc"
result = result and bytearray(b"bc") in b"abc"
result = result and 97 in bytearray(b"abc")
result = result and 200 not in bytearray(b"abc")
result = result and b"ab" in bytearray(b"abc")
result = result and bytearray(b"bc") in bytearray(b"abc")
result = result and b"" in bytearray()
result = result and bytearray() in b""

bytes_large_value = False
try:
    300 in b"abc"
except ValueError:
    bytes_large_value = True

bytes_negative_value = False
try:
    -1 in b"abc"
except ValueError:
    bytes_negative_value = True

bytes_large_not_in = False
try:
    300 not in b"abc"
except ValueError:
    bytes_large_not_in = True

bytes_none_type = False
try:
    None in b"abc"
except TypeError:
    bytes_none_type = True

bytes_float_type = False
try:
    97.0 in b"abc"
except TypeError:
    bytes_float_type = True

bytes_string_type = False
try:
    "a" in b"abc"
except TypeError:
    bytes_string_type = True

bytearray_large_value = False
try:
    300 in bytearray(b"abc")
except ValueError:
    bytearray_large_value = True

bytearray_negative_value = False
try:
    -1 in bytearray(b"abc")
except ValueError:
    bytearray_negative_value = True

bytearray_none_not_in = False
try:
    None not in bytearray(b"abc")
except TypeError:
    bytearray_none_not_in = True

bytearray_string_type = False
try:
    "a" in bytearray(b"abc")
except TypeError:
    bytearray_string_type = True

chained_first_value = False
try:
    300 in b"abc" in [b"abc"]
except ValueError:
    chained_first_value = True

chained_second_type = False
try:
    b"abc" in [b"abc"] in b"abc"
except TypeError:
    chained_second_type = True

result = (
    result
    and bytes_large_value
    and bytes_negative_value
    and bytes_large_not_in
    and bytes_none_type
    and bytes_float_type
    and bytes_string_type
    and bytearray_large_value
    and bytearray_negative_value
    and bytearray_none_not_in
    and bytearray_string_type
    and chained_first_value
    and chained_second_type
)

assert result
result
