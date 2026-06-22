int_ok = False
num = 0
den = 0
match -7:
    case int(numerator=num, denominator=den):
        int_ok = num == -7 and den == 1
    case _:
        int_ok = False

bool_ok = False
bool_num = 0
bool_den = 0
match True:
    case bool(numerator=bool_num, denominator=bool_den):
        bool_ok = bool_num == 1 and bool_den == 1
    case _:
        bool_ok = False

positional_ok = False
whole = 0
whole_num = 0
whole_den = 0
match 6:
    case int(whole, numerator=whole_num, denominator=whole_den):
        positional_ok = whole == 6 and whole_num == 6 and whole_den == 1
    case _:
        positional_ok = False

float_attr = "old"
float_missing_ok = False
match 1.5:
    case float(numerator=float_attr):
        float_missing_ok = False
    case _:
        float_missing_ok = float_attr == "old"

guard_num = "old"
guard_ok = False
match 8:
    case int(numerator=guard_num) if False:
        guard_ok = False
    case _:
        guard_ok = guard_num == 8

result = int_ok and bool_ok and positional_ok and float_missing_ok and guard_ok
assert result
result
