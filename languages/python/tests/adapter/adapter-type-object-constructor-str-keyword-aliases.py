import builtins
from builtins import str as imported_str


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


str_alias = str
str_type = type("")


def str_unknown_keyword():
    str_alias(object=1, foo=2)


def str_duplicate_object_keyword():
    str_alias(object=1, **{"object": 2})


def str_positional_object_conflict():
    str_alias(1, object=2)


def str_object_with_encoding():
    str_alias(object="x", encoding="ascii")


def str_encoding_type_error():
    str_alias(encoding=1)


def str_errors_type_error():
    str_alias(errors=1)


positive = (
    str(object=123) == "123"
    and str_alias(object=True) == "True"
    and str_alias(**{"object": None}) == "None"
    and str_alias(object=b"AB") == "b'AB'"
    and str_alias(**{}) == ""
    and str_alias(123, **{}) == "123"
    and str_alias(encoding="ascii") == ""
    and str_alias(errors="ignore") == ""
    and str_alias(encoding="bad-encoding", errors="bad") == ""
    and builtins.str(object=...) == "Ellipsis"
    and imported_str(object=False) == "False"
    and str_type(object=456) == "456"
    and type("")(object="ok") == "ok"
    and type("")(**{}) == ""
)

errors = (
    mark_type_error(str_unknown_keyword)
    and mark_type_error(str_duplicate_object_keyword)
    and mark_type_error(str_positional_object_conflict)
    and mark_type_error(str_object_with_encoding)
    and mark_type_error(str_encoding_type_error)
    and mark_type_error(str_errors_type_error)
)

result = positive and errors
assert result
result
