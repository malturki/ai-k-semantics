value = 7
width = 4
name = "Ada"
align = ">"
precision = 2

result = f"{value:0{width}d}:{name:{align}{width}s}:{name:.{precision}s}"
assert result == "0007: Ada:Ad"

nested = f"{value:0{width!s}d}:{value:0{width:1d}d}"
assert nested == "0007:0007"

converted = f"{789!s:.{precision}s}:{name!r:>{width + 3}}"
assert converted == "78:  'Ada'"

x = 0
order = f"{(x := 7)!s:0>{(x := x + 1)}}:{x}"
assert order == "00000007:8"

x = 0
value_error_before_spec = False
try:
    f"{1 / 0:{(x := 99)}d}"
except ZeroDivisionError:
    value_error_before_spec = x == 0

assert value_error_before_spec

x = 0
spec_error_after_value = False
try:
    f"{(x := 3):{1 / 0}d}"
except ZeroDivisionError:
    spec_error_after_value = x == 3

assert spec_error_after_value
spec_error_after_value
