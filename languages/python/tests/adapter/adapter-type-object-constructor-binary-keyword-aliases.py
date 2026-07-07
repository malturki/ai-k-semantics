import builtins
from builtins import bytearray as imported_bytearray
from builtins import bytes as imported_bytes
from builtins import memoryview as imported_memoryview


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


bytes_alias = bytes
bytearray_alias = bytearray
memoryview_alias = memoryview

bytes_type = type(b"")
bytearray_type = type(bytearray())
memoryview_type = type(memoryview(b""))


def bytes_unknown_keyword():
    bytes_alias(source=b"A", foo=1)


def bytes_duplicate_source_keyword():
    bytes_alias(source=b"A", **{"source": b"B"})


def bytes_encoding_without_source():
    bytes_alias(encoding="ascii")


def bytes_errors_without_source():
    bytes_alias(errors="ignore")


def bytes_source_errors_without_encoding():
    bytes_alias(source=b"A", errors="ignore")


def bytes_positional_source_conflict():
    bytes_alias(b"A", source=b"B")


def bytes_positional_encoding_conflict():
    bytes_alias("A", "ascii", encoding="latin-1")


def bytes_too_many_positional_with_keyword():
    bytes_alias("A", "ascii", "strict", errors="ignore")


def bytes_mixed_errors_without_encoding():
    bytes_alias([65], errors="ignore")


def bytearray_unknown_keyword():
    bytearray_alias(source=b"A", foo=1)


def bytearray_source_errors_without_encoding():
    bytearray_alias(source=b"A", errors="ignore")


def bytearray_positional_source_conflict():
    bytearray_alias(b"A", source=b"B")


def memoryview_missing_object_keyword():
    memoryview_alias(**{})


def memoryview_unknown_keyword():
    memoryview_alias(object=b"A", foo=1)


def memoryview_duplicate_object_keyword():
    memoryview_alias(object=b"A", **{"object": b"B"})


def memoryview_positional_object_conflict():
    memoryview_alias(b"A", object=b"B")


bytes_positive = (
    bytes_alias(**{}) == b""
    and bytes_alias(source=3) == b"\x00\x00\x00"
    and bytes_alias(source=[65, 66]) == b"AB"
    and bytes_alias(source="A\xe9", encoding="utf-8") == b"A\xc3\xa9"
    and bytes_alias(source="A\xe9", encoding="ascii", errors="ignore") == b"A"
    and bytes_alias("A\xe9", encoding="ascii", errors="ignore") == b"A"
    and bytes_alias("A\xe9", "ascii", errors="ignore") == b"A"
    and builtins.bytes(source=b"CD") == b"CD"
    and imported_bytes(source=bytearray(b"EF")) == b"EF"
    and bytes_type(source=[71]) == b"G"
    and type(b"")(source="H", encoding="ascii") == b"H"
)

bytearray_positive = (
    bytearray_alias(**{}) == bytearray(b"")
    and bytearray_alias(source=3) == bytearray(b"\x00\x00\x00")
    and bytearray_alias(source=[65, 66]) == bytearray(b"AB")
    and bytearray_alias(source="A\xe9", encoding="utf-8") == bytearray(b"A\xc3\xa9")
    and bytearray_alias(source="A\xe9", encoding="ascii", errors="ignore") == bytearray(b"A")
    and bytearray_alias("A\xe9", encoding="ascii", errors="ignore") == bytearray(b"A")
    and bytearray_alias("A\xe9", "ascii", errors="ignore") == bytearray(b"A")
    and builtins.bytearray(source=b"CD") == bytearray(b"CD")
    and imported_bytearray(source=b"EF") == bytearray(b"EF")
    and bytearray_type(source=[71]) == bytearray(b"G")
    and type(bytearray())(source="H", encoding="ascii") == bytearray(b"H")
)

memoryview_positive = (
    list(memoryview_alias(object=b"AB")) == [65, 66]
    and list(memoryview_alias(b"CD", **{})) == [67, 68]
    and list(builtins.memoryview(object=bytearray(b"E"))) == [69]
    and list(imported_memoryview(object=b"F")) == [70]
    and list(memoryview_type(object=b"G")) == [71]
    and list(type(memoryview(b""))(object=bytearray(b"H"))) == [72]
)

errors = (
    mark_type_error(bytes_unknown_keyword)
    and mark_type_error(bytes_duplicate_source_keyword)
    and mark_type_error(bytes_encoding_without_source)
    and mark_type_error(bytes_errors_without_source)
    and mark_type_error(bytes_source_errors_without_encoding)
    and mark_type_error(bytes_positional_source_conflict)
    and mark_type_error(bytes_positional_encoding_conflict)
    and mark_type_error(bytes_too_many_positional_with_keyword)
    and mark_type_error(bytes_mixed_errors_without_encoding)
    and mark_type_error(bytearray_unknown_keyword)
    and mark_type_error(bytearray_source_errors_without_encoding)
    and mark_type_error(bytearray_positional_source_conflict)
    and mark_type_error(memoryview_missing_object_keyword)
    and mark_type_error(memoryview_unknown_keyword)
    and mark_type_error(memoryview_duplicate_object_keyword)
    and mark_type_error(memoryview_positional_object_conflict)
)

result = bytes_positive and bytearray_positive and memoryview_positive and errors
assert result
result
