sign_plus = False
try:
    format("abcdef", "+")
except ValueError:
    sign_plus = True

sign_minus = False
try:
    format("abcdef", "-")
except ValueError:
    sign_minus = True

sign_space = False
try:
    format("abcdef", " ")
except ValueError:
    sign_space = True

sign_width_type = False
try:
    format("abcdef", "+8s")
except ValueError:
    sign_width_type = True

alternate = False
try:
    format("abcdef", "#")
except ValueError:
    alternate = True

alternate_width_type = False
try:
    format("abcdef", "#8s")
except ValueError:
    alternate_width_type = True

equal_align = False
try:
    format("abcdef", "=8")
except ValueError:
    equal_align = True

equal_align_type = False
try:
    format("abcdef", "=8s")
except ValueError:
    equal_align_type = True

equal_fill_align = False
try:
    format("abcdef", "0=8s")
except ValueError:
    equal_fill_align = True

sign_precision = False
try:
    format("abcdef", "+.2s")
except ValueError:
    sign_precision = True

alternate_precision = False
try:
    format("abcdef", "#.2s")
except ValueError:
    alternate_precision = True

equal_precision = False
try:
    format("abcdef", "0=.2s")
except ValueError:
    equal_precision = True

result = (
    sign_plus
    and sign_minus
    and sign_space
    and sign_width_type
    and alternate
    and alternate_width_type
    and equal_align
    and equal_align_type
    and equal_fill_align
    and sign_precision
    and alternate_precision
    and equal_precision
)
assert result
result
