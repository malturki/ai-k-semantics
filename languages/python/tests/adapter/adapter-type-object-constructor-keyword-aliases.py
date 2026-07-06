import builtins
from builtins import complex as imported_complex
from builtins import dict as imported_dict


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


dict_alias = dict
complex_alias = complex
dict_type = type({})
complex_type = type(0j)


def dict_duplicate_kw():
    dict_alias(a=1, **{"a": 2})


def dict_duplicate_mixed_kw():
    dict_type({"a": 0}, a=1, **{"a": 2})


def dict_too_many_pos_mixed():
    dict_alias({}, {}, a=1)


def complex_unknown_kw():
    complex_alias(foo=1)


def complex_duplicate_kw():
    complex_type(real=1, **{"real": 2})


def complex_real_after_positional():
    complex_alias(1, real=2)


def complex_bad_base_mixed():
    complex_alias([], imag=1)


def complex_too_many_pos_mixed():
    complex_alias(1, 2, imag=3)


dict_keyword_aliases = (
    dict_alias(a=1, b=2) == {"a": 1, "b": 2}
    and dict_alias(**{"a": 1}) == {"a": 1}
    and dict_alias({"a": 0, "z": 9}, a=3, c=4) == {"a": 3, "z": 9, "c": 4}
    and dict_alias({"a": 1}, **{}) == {"a": 1}
    and builtins.dict(a=5) == {"a": 5}
    and imported_dict([("x", 1)], y=2) == {"x": 1, "y": 2}
    and dict_type(a=7) == {"a": 7}
    and type({"seed": 0})([("left", 1)], right=2) == {"left": 1, "right": 2}
)

complex_keyword_aliases = (
    complex_alias(real=4.25) == (4.25 + 0j)
    and complex_alias(imag=1.5) == 1.5j
    and complex_alias(**{"real": 4.25, "imag": 1.5}) == (4.25 + 1.5j)
    and complex_alias(**{}) == 0j
    and complex_alias(4.25, imag=1.5) == (4.25 + 1.5j)
    and builtins.complex(real=True, imag=False) == (1 + 0j)
    and imported_complex(4.25, **{"imag": 1.5}) == (4.25 + 1.5j)
    and complex_type(real=4.25, imag=1.5) == (4.25 + 1.5j)
    and type(1j)(4.25, imag=1.5) == (4.25 + 1.5j)
)

errors = (
    mark_type_error(dict_duplicate_kw)
    and mark_type_error(dict_duplicate_mixed_kw)
    and mark_type_error(dict_too_many_pos_mixed)
    and mark_type_error(complex_unknown_kw)
    and mark_type_error(complex_duplicate_kw)
    and mark_type_error(complex_real_after_positional)
    and mark_type_error(complex_bad_base_mixed)
    and mark_type_error(complex_too_many_pos_mixed)
)

result = dict_keyword_aliases and complex_keyword_aliases and errors
assert result
result
