assert ord(" ") == 32
assert ord("A") == 65
assert ord("a") == 97
assert ord(chr(0)) == 0
assert ord(chr(9)) == 9
assert ord(chr(127)) == 127
assert ord(chr(128)) == 128
assert ord(chr(255)) == 255

assert ord(b" ") == 32
assert ord(b"A") == 65
assert ord(b"a") == 97
assert ord(b"\x80") == 128
assert ord(b"\xff") == 255

empty_string_error = False
try:
    ord("")
except TypeError:
    empty_string_error = True

long_string_error = False
try:
    ord("ab")
except TypeError:
    long_string_error = True

empty_bytes_error = False
try:
    ord(b"")
except TypeError:
    empty_bytes_error = True

long_bytes_error = False
try:
    ord(b"ab")
except TypeError:
    long_bytes_error = True

type_error = False
try:
    ord(42)
except TypeError:
    type_error = True

result = empty_string_error and long_string_error and empty_bytes_error and long_bytes_error and type_error
result
