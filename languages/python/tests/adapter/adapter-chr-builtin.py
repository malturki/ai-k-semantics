controls = chr(0) + chr(8) + chr(27) + chr(127)

assert chr(65) == "A"
assert repr(chr(True)) == "'\\x01'"
assert repr(controls) == "'\\x00\\x08\\x1b\\x7f'"
assert ascii(controls) == "'\\x00\\x08\\x1b\\x7f'"
assert f"{controls!r}:{chr(9)!a}" == "'\\x00\\x08\\x1b\\x7f':'\\t'"

low_error = False
try:
    chr(-1)
except ValueError:
    low_error = True

high_error = False
try:
    chr(1114112)
except ValueError:
    high_error = True

type_error = False
try:
    chr("x")
except TypeError:
    type_error = True

result = low_error and high_error and type_error
result
