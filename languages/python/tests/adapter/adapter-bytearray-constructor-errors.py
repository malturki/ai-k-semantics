negative_size = False
try:
    bytearray(-1)
except ValueError:
    negative_size = True

string_without_encoding = False
try:
    bytearray("abc")
except TypeError:
    string_without_encoding = True

float_source = False
try:
    bytearray(1.0)
except TypeError:
    float_source = True

list_string_item = False
try:
    bytearray(["0"])
except TypeError:
    list_string_item = True

list_float_item = False
try:
    bytearray([1.0])
except TypeError:
    list_float_item = True

list_negative_item = False
try:
    bytearray([-1])
except ValueError:
    list_negative_item = True

list_large_item = False
try:
    bytearray([256])
except ValueError:
    list_large_item = True

ascii_encode_error = False
try:
    bytearray("\xe9", "ascii")
except UnicodeEncodeError:
    ascii_encode_error = True

unknown_encoding = False
try:
    bytearray("abc", "missing-codec")
except LookupError:
    unknown_encoding = True

bad_error_handler = False
try:
    bytearray("\xe9", "ascii", "missing-handler")
except LookupError:
    bad_error_handler = True

bad_encoding_type = False
try:
    bytearray("abc", 1)
except TypeError:
    bad_encoding_type = True

bad_errors_type = False
try:
    bytearray("abc", "ascii", 1)
except TypeError:
    bad_errors_type = True

index_error = False
try:
    bytearray(b"a")[5]
except IndexError:
    index_error = True

index_type_error = False
try:
    bytearray(b"a")[1.0]
except TypeError:
    index_type_error = True

zero_slice_step = False
try:
    bytearray(b"a")[::0]
except ValueError:
    zero_slice_step = True

result = (
    negative_size
    and string_without_encoding
    and float_source
    and list_string_item
    and list_float_item
    and list_negative_item
    and list_large_item
    and ascii_encode_error
    and unknown_encoding
    and bad_error_handler
    and bad_encoding_type
    and bad_errors_type
    and index_error
    and index_type_error
    and zero_slice_step
)
assert result
result
