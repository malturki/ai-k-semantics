int_zero_negative = False
try:
    0 ** -1
except ZeroDivisionError:
    int_zero_negative = True

bool_zero_negative = False
try:
    False ** -1
except ZeroDivisionError:
    bool_zero_negative = True

float_zero_negative_int = False
try:
    0.0 ** -1
except ZeroDivisionError:
    float_zero_negative_int = True

int_zero_negative_float = False
try:
    0 ** -1.0
except ZeroDivisionError:
    int_zero_negative_float = True

complex_zero_negative = False
try:
    0j ** -1
except ZeroDivisionError:
    complex_zero_negative = True

pow_int_zero_negative = False
try:
    pow(0, -1)
except ZeroDivisionError:
    pow_int_zero_negative = True

pow_float_zero_negative = False
try:
    pow(0.0, -1)
except ZeroDivisionError:
    pow_float_zero_negative = True

pow_int_zero_negative_float = False
try:
    pow(0, -1.0)
except ZeroDivisionError:
    pow_int_zero_negative_float = True

pow_complex_zero_negative = False
try:
    pow(0j, -1)
except ZeroDivisionError:
    pow_complex_zero_negative = True

pow_mod_zero = False
try:
    pow(2, 3, 0)
except ValueError:
    pow_mod_zero = True

pow_mod_noninvertible = False
try:
    pow(2, -1, 4)
except ValueError:
    pow_mod_noninvertible = True

pow_mod_zero_base_noninvertible = False
try:
    pow(0, -1, 5)
except ValueError:
    pow_mod_zero_base_noninvertible = True

pow_mod_bool_zero_noninvertible = False
try:
    pow(False, -1, 2)
except ValueError:
    pow_mod_bool_zero_noninvertible = True

result = (
    int_zero_negative
    and bool_zero_negative
    and float_zero_negative_int
    and int_zero_negative_float
    and complex_zero_negative
    and pow_int_zero_negative
    and pow_float_zero_negative
    and pow_int_zero_negative_float
    and pow_complex_zero_negative
    and pow_mod_zero
    and pow_mod_noninvertible
    and pow_mod_zero_base_noninvertible
    and pow_mod_bool_zero_noninvertible
)
assert result
result
