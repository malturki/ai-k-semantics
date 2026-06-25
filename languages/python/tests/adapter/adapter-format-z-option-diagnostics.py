int_z_default = False
try:
    format(10, "z")
except ValueError:
    int_z_default = True

int_z_sign = False
try:
    format(10, "+z")
except ValueError:
    int_z_sign = True

int_z_width = False
try:
    format(10, "z8d")
except ValueError:
    int_z_width = True

int_z_zero_width = False
try:
    format(10, "z08d")
except ValueError:
    int_z_zero_width = True

int_z_alternate = False
try:
    format(10, "z#x")
except ValueError:
    int_z_alternate = True

bool_z = False
try:
    format(True, "z")
except ValueError:
    bool_z = True

string_z_default = False
try:
    format("abcdef", "z")
except ValueError:
    string_z_default = True

string_z_type = False
try:
    format("abcdef", "zs")
except ValueError:
    string_z_type = True

string_z_width = False
try:
    format("abcdef", "z8s")
except ValueError:
    string_z_width = True

string_z_align = False
try:
    format("abcdef", ">z8s")
except ValueError:
    string_z_align = True

string_z_fill_align = False
try:
    format("abcdef", "0>z8s")
except ValueError:
    string_z_fill_align = True

string_z_precision = False
try:
    format("abcdef", "z.2s")
except ValueError:
    string_z_precision = True

result = (
    int_z_default
    and int_z_sign
    and int_z_width
    and int_z_zero_width
    and int_z_alternate
    and bool_z
    and string_z_default
    and string_z_type
    and string_z_width
    and string_z_align
    and string_z_fill_align
    and string_z_precision
)
assert result
result
