kw_then_unpack = False
try:
    dict(a=1, **{"a": 2})
except TypeError:
    kw_then_unpack = True

unpack_then_kw = False
try:
    dict(**{"a": 1}, a=2)
except TypeError:
    unpack_then_kw = True

two_unpacks = False
try:
    dict(**{"a": 1}, **{"a": 2})
except TypeError:
    two_unpacks = True

base_kw_override = dict({"a": 1}, a=2)["a"] == 2
base_unpack_override = dict({"a": 1}, **{"a": 2})["a"] == 2
distinct_unpacks = dict(**{"a": 1}, **{"b": 2}) == {"a": 1, "b": 2}

kw_value_exception = False
try:
    dict(a=range(1, 5, 0))
except ValueError:
    kw_value_exception = True

result = (
    kw_then_unpack
    and unpack_then_kw
    and two_unpacks
    and base_kw_override
    and base_unpack_override
    and distinct_unpacks
    and kw_value_exception
)
assert result
result
