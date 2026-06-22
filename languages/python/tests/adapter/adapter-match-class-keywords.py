complex_ok = False
real = 0.0
imag = 0.0
match 3 + 4j:
    case complex(real=real, imag=imag):
        complex_ok = real == 3.0 and imag == 4.0
    case _:
        complex_ok = False

int_ok = False
whole = 0
real_int = 0
imag_int = 99
match 3:
    case int(whole, real=real_int, imag=imag_int):
        int_ok = whole == 3 and real_int == 3 and imag_int == 0
    case _:
        int_ok = False

range_ok = False
start = 0
stop = 0
step = 0
match range(2, 8, 3):
    case range(start=start, stop=stop, step=step):
        range_ok = start == 2 and stop == 8 and step == 3
    case _:
        range_ok = False

slice_ok = False
lower = 0
upper = 0
stride = 0
match slice(1, 5, 2):
    case slice(start=lower, stop=upper, step=stride):
        slice_ok = lower == 1 and upper == 5 and stride == 2
    case _:
        slice_ok = False

nested_ok = False
nested_real = 0
match 5:
    case int(real=int(nested_real)):
        nested_ok = nested_real == 5
    case _:
        nested_ok = False

unchanged = "old"
unchanged_whole = "old-whole"
failed_ok = False
match "not an int":
    case int(unchanged_whole, real=unchanged):
        failed_ok = False
    case _:
        failed_ok = unchanged == "old" and unchanged_whole == "old-whole"

guard_whole = "old"
guard_real = "old"
guard_ok = False
match 4:
    case int(guard_whole, real=guard_real) if False:
        guard_ok = False
    case _:
        guard_ok = guard_whole == 4 and guard_real == 4

missing_attr = "old"
missing_ok = False
match 3:
    case int(start=missing_attr):
        missing_ok = False
    case _:
        missing_ok = missing_attr == "old"

result = (
    complex_ok
    and int_ok
    and range_ok
    and slice_ok
    and nested_ok
    and failed_ok
    and guard_ok
    and missing_ok
)
assert result
result
