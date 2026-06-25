operator_str_base = False
try:
    "a" ** 2
except TypeError:
    operator_str_base = True

operator_str_exp = False
try:
    2 ** "a"
except TypeError:
    operator_str_exp = True

operator_none_base = False
try:
    None ** 2
except TypeError:
    operator_none_base = True

operator_none_exp = False
try:
    2 ** None
except TypeError:
    operator_none_exp = True

pow_str_base = False
try:
    pow("a", 2)
except TypeError:
    pow_str_base = True

pow_str_exp = False
try:
    pow(2, "a")
except TypeError:
    pow_str_exp = True

pow_none_base = False
try:
    pow(None, 2)
except TypeError:
    pow_none_base = True

pow_none_exp = False
try:
    pow(2, None)
except TypeError:
    pow_none_exp = True

pow_list_base = False
try:
    pow([], 2)
except TypeError:
    pow_list_base = True

pow_list_exp = False
try:
    pow(2, [])
except TypeError:
    pow_list_exp = True

pow_mod_str_base = False
try:
    pow("a", 2, 3)
except TypeError:
    pow_mod_str_base = True

pow_mod_str_exp = False
try:
    pow(2, "a", 3)
except TypeError:
    pow_mod_str_exp = True

pow_mod_str_mod = False
try:
    pow(2, 3, "a")
except TypeError:
    pow_mod_str_mod = True

pow_mod_float_base = False
try:
    pow(2.0, 3, 5)
except TypeError:
    pow_mod_float_base = True

pow_mod_float_exp = False
try:
    pow(2, 3.0, 5)
except TypeError:
    pow_mod_float_exp = True

pow_mod_float_mod = False
try:
    pow(2, 3, 5.0)
except TypeError:
    pow_mod_float_mod = True

result = (
    operator_str_base
    and operator_str_exp
    and operator_none_base
    and operator_none_exp
    and pow_str_base
    and pow_str_exp
    and pow_none_base
    and pow_none_exp
    and pow_list_base
    and pow_list_exp
    and pow_mod_str_base
    and pow_mod_str_exp
    and pow_mod_str_mod
    and pow_mod_float_base
    and pow_mod_float_exp
    and pow_mod_float_mod
)
assert result
result
