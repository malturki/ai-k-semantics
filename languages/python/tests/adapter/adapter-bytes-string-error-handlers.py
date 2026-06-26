text = "A\xe9\u03a9\U0001f600"
latin_text = "A\xe9\u0100\U0001f600"

result = bytes(text, "ascii", "ignore") == b"A"
result = result and bytes(text, "ascii", "replace") == b"A???"
result = result and bytes(latin_text, "latin-1", "ignore") == b"A\xe9"
result = result and bytes(latin_text, "latin-1", "replace") == b"A\xe9??"
result = result and bytes(text, "utf-8", "ignore") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"
result = result and bytes(text, "utf-8", "replace") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"

result = result and bytes("abc", "ascii", "made-up-handler") == b"abc"
result = result and bytes("abc", "ascii", "STRICT") == b"abc"
result = result and bytes(text, "utf-8", "made-up-handler") == b"A\xc3\xa9\xce\xa9\xf0\x9f\x98\x80"

lookup_error = False
try:
    bytes("\xe9", "ascii", "STRICT")
except LookupError:
    lookup_error = True

unknown_error_handler = False
try:
    bytes("\xe9", "ascii", "made-up-handler")
except LookupError:
    unknown_error_handler = True

surrogateescape_error = False
try:
    bytes("\xe9", "ascii", "surrogateescape")
except UnicodeEncodeError:
    surrogateescape_error = True

surrogatepass_error = False
try:
    bytes("\u0100", "latin-1", "surrogatepass")
except UnicodeEncodeError:
    surrogatepass_error = True

errors_type_error = False
try:
    bytes("abc", "ascii", 10)
except TypeError:
    errors_type_error = True

result = result and lookup_error and unknown_error_handler
result = result and surrogateescape_error and surrogatepass_error and errors_type_error

assert result
result
