int_bad_string = False
try:
    int("abc")
except ValueError:
    int_bad_string = True

int_empty_string = False
try:
    int("   ")
except ValueError:
    int_empty_string = True

int_bad_base0_digit = False
try:
    int("0b2", 0)
except ValueError:
    int_bad_base0_digit = True

int_base_too_low = False
try:
    int("10", 1)
except ValueError:
    int_base_too_low = True

int_base_too_high = False
try:
    int("10", 37)
except ValueError:
    int_base_too_high = True

int_base_type_error = False
try:
    int("10", "2")
except TypeError:
    int_base_type_error = True

int_explicit_base_non_string = False
try:
    int(10, 2)
except TypeError:
    int_explicit_base_non_string = True

int_bad_bytes = False
try:
    int(b"12z")
except ValueError:
    int_bad_bytes = True

int_bad_bytearray = False
try:
    int(bytearray(b"12z"))
except ValueError:
    int_bad_bytearray = True

float_bad_string = False
try:
    float("abc")
except ValueError:
    float_bad_string = True

float_empty_string = False
try:
    float("   ")
except ValueError:
    float_empty_string = True

float_bad_underscore = False
try:
    float("1__0")
except ValueError:
    float_bad_underscore = True

float_hex_like = False
try:
    float("0x10")
except ValueError:
    float_hex_like = True

float_bad_bytes = False
try:
    float(b"abc")
except ValueError:
    float_bad_bytes = True

float_bad_bytearray = False
try:
    float(bytearray(b"abc"))
except ValueError:
    float_bad_bytearray = True

float_list_type = False
try:
    float([])
except TypeError:
    float_list_type = True

result = (
    int_bad_string
    and int_empty_string
    and int_bad_base0_digit
    and int_base_too_low
    and int_base_too_high
    and int_base_type_error
    and int_explicit_base_non_string
    and int_bad_bytes
    and int_bad_bytearray
    and float_bad_string
    and float_empty_string
    and float_bad_underscore
    and float_hex_like
    and float_bad_bytes
    and float_bad_bytearray
    and float_list_type
)
assert result
result
