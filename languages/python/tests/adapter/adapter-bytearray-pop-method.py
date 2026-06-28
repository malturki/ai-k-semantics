data = bytearray(b"abcd")

last = data.pop()
first = data.pop(0)
negative = data.pop(-1)
zero_bool = data.pop(False)

ordered_ok = (
    last == 100
    and first == 97
    and negative == 99
    and zero_bool == 98
    and data == bytearray()
)

bool_data = bytearray(b"yz")
true_bool = bool_data.pop(True)
bool_ok = true_bool == 122 and bool_data == bytearray(b"y")

errors_ok = True
error_data = bytearray(b"xy")

try:
    data.pop()
except IndexError:
    pass
else:
    errors_ok = False

try:
    error_data.pop(2)
except IndexError:
    pass
else:
    errors_ok = False

try:
    error_data.pop(-3)
except IndexError:
    pass
else:
    errors_ok = False

try:
    error_data.pop(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.pop("0")
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and error_data == bytearray(b"xy")

result = ordered_ok and bool_ok and errors_ok
assert result
result
