bad_default = False
try:
    bad = b"\xff"
    bad.decode()
except UnicodeDecodeError:
    bad_default = True

bad_utf8 = False
try:
    bad = b"\xc3("
    bad.decode("utf-8")
except UnicodeDecodeError:
    bad_utf8 = True

bad_ascii = False
try:
    bad = b"\x80"
    bad.decode("ascii")
except UnicodeDecodeError:
    bad_ascii = True

unknown_encoding = False
try:
    data = b"a"
    data.decode("made-up-codec")
except LookupError:
    unknown_encoding = True

valid = b"a"
unknown_handler_valid = valid.decode("utf-8", "made-up-handler") == "a"

unknown_handler_invalid = False
try:
    bad = b"\xff"
    bad.decode("utf-8", "made-up-handler")
except LookupError:
    unknown_handler_invalid = True

encoding_type_error = False
try:
    data = b"a"
    data.decode(123)
except TypeError:
    encoding_type_error = True

errors_type_error = False
try:
    data = b"a"
    data.decode("utf-8", 123)
except TypeError:
    errors_type_error = True

result = bad_default and bad_utf8 and bad_ascii
result = result and unknown_encoding and unknown_handler_valid and unknown_handler_invalid
result = result and encoding_type_error and errors_type_error

assert result
result
