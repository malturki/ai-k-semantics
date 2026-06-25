pos = float("inf")
neg = float("-inf")
nan = float("nan")

dot_e_error = False
try:
    format(pos, ".e")
except ValueError:
    dot_e_error = True

width_dot_f_error = False
try:
    format(neg, "8.f")
except ValueError:
    width_dot_f_error = True

z_dot_g_error = False
try:
    format(nan, "z.g")
except ValueError:
    z_dot_g_error = True

sign_dot_e_error = False
try:
    format(pos, "+.E")
except ValueError:
    sign_dot_e_error = True

alt_dot_g_error = False
try:
    format(neg, "#.G")
except ValueError:
    alt_dot_g_error = True

zero_dot_percent_error = False
try:
    format(nan, "0.%")
except ValueError:
    zero_dot_percent_error = True

dot_n_error = False
try:
    format(pos, ".n")
except ValueError:
    dot_n_error = True

result = (
    dot_e_error
    and width_dot_f_error
    and z_dot_g_error
    and sign_dot_e_error
    and alt_dot_g_error
    and zero_dot_percent_error
    and dot_n_error
)

assert result
result
