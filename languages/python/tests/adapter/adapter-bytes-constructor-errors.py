negative_size = False
try:
    bytes(-1)
except ValueError:
    negative_size = True

string_without_encoding = False
try:
    bytes("abc")
except TypeError:
    string_without_encoding = True

float_source = False
try:
    bytes(1.0)
except TypeError:
    float_source = True

list_string_item = False
try:
    bytes(["0"])
except TypeError:
    list_string_item = True

list_float_item = False
try:
    bytes([1.0])
except TypeError:
    list_float_item = True

list_negative_item = False
try:
    bytes([-1])
except ValueError:
    list_negative_item = True

list_large_item = False
try:
    bytes([256])
except ValueError:
    list_large_item = True

tuple_large_item = False
try:
    bytes((257,))
except ValueError:
    tuple_large_item = True

range_large_item = False
try:
    bytes(range(254, 257))
except ValueError:
    range_large_item = True

dict_string_key = False
try:
    bytes({"a": 1})
except TypeError:
    dict_string_key = True

dict_large_key = False
try:
    bytes({256: 1})
except ValueError:
    dict_large_key = True

result = (
    negative_size
    and string_without_encoding
    and float_source
    and list_string_item
    and list_float_item
    and list_negative_item
    and list_large_item
    and tuple_large_item
    and range_large_item
    and dict_string_key
    and dict_large_key
)
assert result
result
