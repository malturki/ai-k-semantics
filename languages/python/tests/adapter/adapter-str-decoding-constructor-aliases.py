import builtins
from builtins import str as imported_str


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


def mark_lookup_error(thunk):
    try:
        thunk()
    except LookupError:
        return True
    return False


def mark_unicode_decode_error(thunk):
    try:
        thunk()
    except UnicodeDecodeError:
        return True
    return False


str_alias = str
str_type = type("")


def unicode_decode_error_positional():
    str_alias(b"\xff", "ascii")


def unicode_decode_error_keyword():
    str_alias(b"\xff", encoding="ascii")


def unknown_encoding():
    str_alias(b"A", "missing-codec")


def unknown_error_handler_on_failure():
    str_alias(b"\xff", "ascii", errors="missing-handler")


def non_bytes_object_with_encoding():
    str_alias(123, "ascii")


def string_object_with_encoding():
    str_alias(object="x", encoding="ascii")


def encoding_type_error():
    str_alias(b"x", 1)


def errors_type_error():
    str_alias(b"x", "ascii", 1)


def positional_object_conflict():
    str_alias(b"x", object=b"y")


def positional_encoding_conflict():
    str_alias(b"x", "ascii", encoding="latin-1")


def duplicate_encoding_keyword():
    str_alias(b"x", encoding="ascii", **{"encoding": "latin-1"})


def too_many_positional_with_keyword():
    str_alias(b"x", "ascii", "strict", errors="ignore")


def unknown_keyword():
    str_alias(object=b"x", foo=1)


def duplicate_object_keyword():
    str_alias(object=b"x", **{"object": b"y"})


positive = (
    str(b"A\xc3\xa9", "utf-8") == "A\xe9"
    and str(bytearray(b"A\xe9"), "latin-1") == "A\xe9"
    and str(memoryview(b"A"), "ascii") == "A"
    and str_alias(b"A\xe9", encoding="ascii", errors="ignore") == "A"
    and str_alias(b"\xff", errors="ignore") == ""
    and str_alias(b"\xff", "ascii", errors="backslashreplace") == "\\xff"
    and str_alias(b"A", "ascii", "missing-handler") == "A"
    and str_alias(object=b"B", encoding="ascii") == "B"
    and str_alias(object=bytearray(b"\xff"), encoding="ascii", errors="replace") == "\ufffd"
    and builtins.str(object=memoryview(b"C"), encoding="ascii") == "C"
    and imported_str(b"D", "ascii") == "D"
    and str_type(b"E", "ascii") == "E"
    and type("")(object=b"F", errors="ignore") == "F"
)

errors = (
    mark_unicode_decode_error(unicode_decode_error_positional)
    and mark_unicode_decode_error(unicode_decode_error_keyword)
    and mark_lookup_error(unknown_encoding)
    and mark_lookup_error(unknown_error_handler_on_failure)
    and mark_type_error(non_bytes_object_with_encoding)
    and mark_type_error(string_object_with_encoding)
    and mark_type_error(encoding_type_error)
    and mark_type_error(errors_type_error)
    and mark_type_error(positional_object_conflict)
    and mark_type_error(positional_encoding_conflict)
    and mark_type_error(duplicate_encoding_keyword)
    and mark_type_error(too_many_positional_with_keyword)
    and mark_type_error(unknown_keyword)
    and mark_type_error(duplicate_object_keyword)
)

result = positive and errors
assert result
result
