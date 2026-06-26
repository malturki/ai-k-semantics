text = "A\xe9\u03a9\U0001f600"

result = bytes(text, "utf-8") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"
result = result and bytes(text, "utf8") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"
result = result and bytes(text, "UTF-8", "strict") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"
result = result and bytes("abc", "ascii") == b"abc"
result = result and bytes("abc", "ASCII", "strict") == b"abc"
result = result and bytes("\xff\xe9", "latin-1") == b"\xff\xe9"
result = result and bytes("\xff\xe9", "latin_1", "strict") == b"\xff\xe9"
result = result and bytes("\xff", "iso-8859-1") == b"\xff"
result = result and bytes("", "utf-8") == b""

ascii_error = False
try:
    bytes("\xe9", "ascii")
except UnicodeEncodeError:
    ascii_error = True

latin_error = False
try:
    bytes("\u0100", "latin-1")
except UnicodeEncodeError:
    latin_error = True

lookup_error = False
try:
    bytes("abc", "made-up-codec")
except LookupError:
    lookup_error = True

source_type_error = False
try:
    bytes(3, "utf-8")
except TypeError:
    source_type_error = True

encoding_type_error = False
try:
    bytes("abc", 10)
except TypeError:
    encoding_type_error = True

result = result and ascii_error and latin_error and lookup_error
result = result and source_type_error and encoding_type_error

assert result
result
