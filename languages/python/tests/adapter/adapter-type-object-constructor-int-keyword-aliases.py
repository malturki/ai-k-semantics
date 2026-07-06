import builtins
from builtins import int as imported_int


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


int_alias = int
int_type = type(1)


def int_missing_string_for_base():
    int_alias(base=2)


def int_unknown_keyword():
    int_alias("10", radix=2)


def int_duplicate_base_keyword():
    int_alias("10", base=2, **{"base": 10})


def int_too_many_with_base():
    int_alias("10", 2, base=10)


def int_non_string_with_base():
    int_alias(10, base=2)


def int_bad_base_type():
    int_alias("10", base="2")


def int_base_too_low():
    int_alias("10", base=1)


def int_bad_value_for_base():
    int_alias("zz", base=10)


positive = (
    int("101", base=2) == 5
    and int_alias("ff", base=16) == 255
    and int_alias(b"101", base=2) == 5
    and int_alias(bytearray(b"101"), base=2) == 5
    and int_alias("10", 2, **{}) == 2
    and builtins.int("0x10", base=0) == 16
    and imported_int("z", **{"base": 36}) == 35
    and int_type("12", **{}) == 12
    and int_type(**{}) == 0
    and type(1)("77", base=8) == 63
)

errors = (
    mark_type_error(int_missing_string_for_base)
    and mark_type_error(int_unknown_keyword)
    and mark_type_error(int_duplicate_base_keyword)
    and mark_type_error(int_too_many_with_base)
    and mark_type_error(int_non_string_with_base)
    and mark_type_error(int_bad_base_type)
    and mark_value_error(int_base_too_low)
    and mark_value_error(int_bad_value_for_base)
)

result = positive and errors
assert result
result
