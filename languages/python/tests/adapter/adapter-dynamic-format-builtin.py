spec = "0" + "4d"
result = format(7, spec) == "0007"

hex_spec = "#" + "06x"
result = result and format(10, hex_spec) == "0x000a"

string_spec = "*" + "^" + "8.3s"
result = result and format("abcdef", string_spec) == "**abc***"

spec_type_error = False
try:
    format(7, len("abc"))
except TypeError:
    spec_type_error = True
result = result and spec_type_error

spec_eval_error = False
try:
    format(7, 1 // 0)
except ZeroDivisionError:
    spec_eval_error = True
result = result and spec_eval_error

value_eval_error = False
try:
    format(1 // 0, "d")
except ZeroDivisionError:
    value_eval_error = True
result = result and value_eval_error

result
