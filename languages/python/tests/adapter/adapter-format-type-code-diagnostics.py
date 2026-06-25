int_string_type = False
try:
    format(10, "s")
except ValueError:
    int_string_type = True

int_string_type_width = False
try:
    format(10, "8s")
except ValueError:
    int_string_type_width = True

int_string_type_align = False
try:
    format(10, ">8s")
except ValueError:
    int_string_type_align = True

int_string_type_fill_align = False
try:
    format(10, "0>8s")
except ValueError:
    int_string_type_fill_align = True

int_string_type_sign = False
try:
    format(10, "+s")
except ValueError:
    int_string_type_sign = True

int_string_type_alt = False
try:
    format(10, "#s")
except ValueError:
    int_string_type_alt = True

int_string_type_precision = False
try:
    format(10, ".2s")
except ValueError:
    int_string_type_precision = True

bool_string_type = False
try:
    format(True, "s")
except ValueError:
    bool_string_type = True

string_decimal_type = False
try:
    format("abcdef", "d")
except ValueError:
    string_decimal_type = True

string_decimal_width = False
try:
    format("abcdef", "8d")
except ValueError:
    string_decimal_width = True

string_decimal_align = False
try:
    format("abcdef", ">8d")
except ValueError:
    string_decimal_align = True

string_decimal_fill_align = False
try:
    format("abcdef", "0>8d")
except ValueError:
    string_decimal_fill_align = True

string_binary_type = False
try:
    format("abcdef", "b")
except ValueError:
    string_binary_type = True

string_char_type = False
try:
    format("abcdef", "c")
except ValueError:
    string_char_type = True

string_hex_type = False
try:
    format("abcdef", "x")
except ValueError:
    string_hex_type = True

string_octal_type = False
try:
    format("abcdef", "o")
except ValueError:
    string_octal_type = True

string_float_type = False
try:
    format("abcdef", "f")
except ValueError:
    string_float_type = True

string_general_type = False
try:
    format("abcdef", "g")
except ValueError:
    string_general_type = True

string_percent_type = False
try:
    format("abcdef", "%")
except ValueError:
    string_percent_type = True

string_number_type = False
try:
    format("abcdef", "n")
except ValueError:
    string_number_type = True

string_float_precision = False
try:
    format("abcdef", ".2f")
except ValueError:
    string_float_precision = True

string_float_width_precision = False
try:
    format("abcdef", "8.2f")
except ValueError:
    string_float_width_precision = True

string_decimal_underscore = False
try:
    format("abcdef", "_d")
except ValueError:
    string_decimal_underscore = True

string_decimal_comma = False
try:
    format("abcdef", ",d")
except ValueError:
    string_decimal_comma = True

result = (
    int_string_type
    and int_string_type_width
    and int_string_type_align
    and int_string_type_fill_align
    and int_string_type_sign
    and int_string_type_alt
    and int_string_type_precision
    and bool_string_type
    and string_decimal_type
    and string_decimal_width
    and string_decimal_align
    and string_decimal_fill_align
    and string_binary_type
    and string_char_type
    and string_hex_type
    and string_octal_type
    and string_float_type
    and string_general_type
    and string_percent_type
    and string_number_type
    and string_float_precision
    and string_float_width_precision
    and string_decimal_underscore
    and string_decimal_comma
)
assert result
result
