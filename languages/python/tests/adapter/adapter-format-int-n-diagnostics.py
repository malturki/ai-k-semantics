z_n = False
try:
    format(1234567, "zn")
except ValueError:
    z_n = True

z_width_n = False
try:
    format(1234567, "z8n")
except ValueError:
    z_width_n = True

sign_z_n = False
try:
    format(1234567, "+zn")
except ValueError:
    sign_z_n = True

z_alternate_n = False
try:
    format(1234567, "z#n")
except ValueError:
    z_alternate_n = True

comma_n = False
try:
    format(1234567, ",n")
except ValueError:
    comma_n = True

underscore_n = False
try:
    format(1234567, "_n")
except ValueError:
    underscore_n = True

width_comma_n = False
try:
    format(1234567, "8,n")
except ValueError:
    width_comma_n = True

width_underscore_n = False
try:
    format(1234567, "8_n")
except ValueError:
    width_underscore_n = True

precision_n = False
try:
    format(1234567, ".2n")
except ValueError:
    precision_n = True

width_precision_n = False
try:
    format(1234567, "8.2n")
except ValueError:
    width_precision_n = True

align_precision_n = False
try:
    format(1234567, ">.2n")
except ValueError:
    align_precision_n = True

precision_comma_n = False
try:
    format(1234567, ".,n")
except ValueError:
    precision_comma_n = True

precision_underscore_n = False
try:
    format(1234567, "._n")
except ValueError:
    precision_underscore_n = True

bool_comma_n = False
try:
    format(True, ",n")
except ValueError:
    bool_comma_n = True

result = (
    z_n
    and z_width_n
    and sign_z_n
    and z_alternate_n
    and comma_n
    and underscore_n
    and width_comma_n
    and width_underscore_n
    and precision_n
    and width_precision_n
    and align_precision_n
    and precision_comma_n
    and precision_underscore_n
    and bool_comma_n
)
assert result
result
