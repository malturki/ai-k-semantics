true_div_int = False
try:
    1 / 0
except ZeroDivisionError:
    true_div_int = True

true_div_bool = False
try:
    1 / False
except ZeroDivisionError:
    true_div_bool = True

true_div_float = False
try:
    1.0 / 0.0
except ZeroDivisionError:
    true_div_float = True

true_div_int_float = False
try:
    1 / 0.0
except ZeroDivisionError:
    true_div_int_float = True

true_div_complex = False
try:
    (1 + 2j) / 0j
except ZeroDivisionError:
    true_div_complex = True

true_div_complex_int = False
try:
    (1 + 2j) / 0
except ZeroDivisionError:
    true_div_complex_int = True

true_div_int_complex = False
try:
    1 / 0j
except ZeroDivisionError:
    true_div_int_complex = True

floor_div_int = False
try:
    1 // 0
except ZeroDivisionError:
    floor_div_int = True

floor_div_float = False
try:
    1.0 // 0.0
except ZeroDivisionError:
    floor_div_float = True

floor_div_int_float = False
try:
    1 // 0.0
except ZeroDivisionError:
    floor_div_int_float = True

mod_int = False
try:
    1 % 0
except ZeroDivisionError:
    mod_int = True

mod_float = False
try:
    1.0 % 0.0
except ZeroDivisionError:
    mod_float = True

mod_int_float = False
try:
    1 % 0.0
except ZeroDivisionError:
    mod_int_float = True

divmod_int = False
try:
    divmod(1, 0)
except ZeroDivisionError:
    divmod_int = True

divmod_float = False
try:
    divmod(1.0, 0.0)
except ZeroDivisionError:
    divmod_float = True

divmod_int_float = False
try:
    divmod(1, 0.0)
except ZeroDivisionError:
    divmod_int_float = True

result = (
    true_div_int
    and true_div_bool
    and true_div_float
    and true_div_int_float
    and true_div_complex
    and true_div_complex_int
    and true_div_int_complex
    and floor_div_int
    and floor_div_float
    and floor_div_int_float
    and mod_int
    and mod_float
    and mod_int_float
    and divmod_int
    and divmod_float
    and divmod_int_float
)
assert result
result
