data = b"banana"

value_error_ok = True
try:
    data.find(300, 0, 1)
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.count("a", 0, 1)
    type_error_ok = False
except TypeError:
    pass

try:
    data.find(b"a", "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rfind(b"a", 0, "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.index(300, "x")
    type_error_ok = False
except TypeError:
    pass

result = value_error_ok and type_error_ok and data == b"banana"
assert result
result
