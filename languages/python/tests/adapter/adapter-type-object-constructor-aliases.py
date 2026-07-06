import builtins
from builtins import bytes as imported_bytes
from builtins import int as imported_int
from builtins import range as imported_range


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


def mark_value_error(thunk):
    try:
        thunk()
    except ValueError:
        return True
    return False


bool_alias = bool
int_alias = int
float_alias = float
complex_alias = complex
str_alias = str
bytes_alias = bytes
bytearray_alias = bytearray
list_alias = list
tuple_alias = tuple
dict_alias = dict
set_alias = set
frozenset_alias = frozenset
range_alias = range
slice_alias = slice
memoryview_alias = memoryview


def range_zero_args():
    range_alias()


def slice_zero_args():
    slice_alias()


def memoryview_zero_args():
    memoryview_alias()


def int_bad_base():
    int_alias("10", "x")


def int_bad_value():
    int_alias("zz", 10)


def bytes_string_no_encoding():
    bytes_alias("x")


def range_too_many_args():
    range_alias(1, 2, 3, 4)


one_arg_aliases = (
    bool_alias(1) is True
    and int_alias("42") == 42
    and float_alias("1.5") == 1.5
    and complex_alias("1+2j") == 1 + 2j
    and str_alias(123) == "123"
    and bytes_alias([65, 66]) == b"AB"
    and bytearray_alias([65, 66]) == bytearray(b"AB")
    and list_alias("ab") == ["a", "b"]
    and tuple_alias("ab") == ("a", "b")
    and dict_alias({"x": 1}) == {"x": 1}
    and set_alias([1, 1, 2]) == {1, 2}
    and frozenset_alias([1, 1, 2]) == frozenset({1, 2})
    and list_alias(range_alias(3)) == [0, 1, 2]
    and list_alias(memoryview_alias(b"AB")) == [65, 66]
)

multi_arg_aliases = (
    int_alias("101", 2) == 5
    and complex_alias(1, 2) == 1 + 2j
    and bytes_alias("AB", "ascii") == b"AB"
    and bytes_alias("A", "ascii", "strict") == b"A"
    and bytearray_alias("AB", "ascii") == bytearray(b"AB")
    and bytearray_alias("A", "ascii", "strict") == bytearray(b"A")
    and list_alias(range_alias(1, 6, 2)) == [1, 3, 5]
)

slice_from_alias = slice_alias(1, 6, 2)
slice_two_arg = slice_alias(2, 5)
slice_aliases = (
    slice_from_alias.start == 1
    and slice_from_alias.stop == 6
    and slice_from_alias.step == 2
    and slice_two_arg.start == 2
    and slice_two_arg.stop == 5
    and slice_two_arg.step is None
)

module_aliases = (
    builtins.int("11", 2) == 3
    and builtins.bytes("A", "ascii") == b"A"
    and builtins.list((1, 2)) == [1, 2]
    and list_alias(builtins.range(2, 5)) == [2, 3, 4]
)

from_import_aliases = (
    imported_int("10", 2) == 2
    and imported_bytes("B", "ascii") == b"B"
    and list_alias(imported_range(2, 5)) == [2, 3, 4]
)

int_type = type(1)
list_type = type([])
range_type = type(range(1))
slice_type = type(slice(1))
dynamic_type_aliases = (
    int_type("12") == 12
    and list_type((1, 2)) == [1, 2]
    and list_type(range_type(3)) == [0, 1, 2]
    and slice_type(1, 4, 2).step == 2
)

errors = (
    mark_type_error(range_zero_args)
    and mark_type_error(slice_zero_args)
    and mark_type_error(memoryview_zero_args)
    and mark_type_error(int_bad_base)
    and mark_value_error(int_bad_value)
    and mark_type_error(bytes_string_no_encoding)
    and mark_type_error(range_too_many_args)
)

result = (
    one_arg_aliases
    and multi_arg_aliases
    and slice_aliases
    and module_aliases
    and from_import_aliases
    and dynamic_type_aliases
    and errors
)

result
