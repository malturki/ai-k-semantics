default_precision_error = False
try:
    format(10, ".3")
except ValueError:
    default_precision_error = True

decimal_precision_error = False
try:
    format(10, ".3d")
except ValueError:
    decimal_precision_error = True

width_precision_error = False
try:
    format(10, "5.3d")
except ValueError:
    width_precision_error = True

binary_precision_error = False
try:
    format(10, ".3b")
except ValueError:
    binary_precision_error = True

alternate_precision_error = False
try:
    format(10, "#8.3x")
except ValueError:
    alternate_precision_error = True

sign_zero_precision_error = False
try:
    format(-10, "+08.3d")
except ValueError:
    sign_zero_precision_error = True

char_precision_error = False
try:
    format(65, ".3c")
except ValueError:
    char_precision_error = True

comma_precision_error = False
try:
    format(1234567, ".3,d")
except ValueError:
    comma_precision_error = True

underscore_precision_error = False
try:
    format(0x12345678, ".3_x")
except ValueError:
    underscore_precision_error = True

bool_precision_error = False
try:
    format(True, ".3d")
except ValueError:
    bool_precision_error = True

missing_precision_error = False
try:
    format(10, ".")
except ValueError:
    missing_precision_error = True

missing_type_precision_error = False
try:
    format(10, ".d")
except ValueError:
    missing_type_precision_error = True

missing_width_precision_error = False
try:
    format(10, "5.")
except ValueError:
    missing_width_precision_error = True

missing_alternate_precision_error = False
try:
    format(10, "#.x")
except ValueError:
    missing_alternate_precision_error = True

result = default_precision_error
result = result and decimal_precision_error
result = result and width_precision_error
result = result and binary_precision_error
result = result and alternate_precision_error
result = result and sign_zero_precision_error
result = result and char_precision_error
result = result and comma_precision_error
result = result and underscore_precision_error
result = result and bool_precision_error
result = result and missing_precision_error
result = result and missing_type_precision_error
result = result and missing_width_precision_error
result = result and missing_alternate_precision_error

assert result
result
