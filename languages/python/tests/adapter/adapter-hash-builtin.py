integer_ok = (
    hash(0) == 0
    and hash(1) == 1
    and hash(-1) == -2
    and hash(True) == hash(1)
    and hash(False) == hash(0)
)

numeric_equality_ok = (
    hash(1) == hash(1.0)
    and hash(1) == hash(complex(1, 0))
    and hash(-2) == hash(-2.0)
    and hash(-2) == hash(complex(-2, 0))
    and hash(0.5) == hash(complex(0.5, 0))
)

string_bytes_ok = (
    hash("") == 0
    and hash(b"") == 0
    and hash("spam") == hash(b"spam")
    and isinstance(hash("eggs"), int)
)

tuple_ok = (
    hash((1, "a")) == hash((True, "a"))
    and hash((1, 2, 3)) == hash((1, 2, 3))
    and isinstance(hash(()), int)
)

frozenset_ok = (
    hash(frozenset("abc")) == hash(frozenset("cba"))
    and hash(frozenset([1, True])) == hash(frozenset([1]))
    and isinstance(hash(frozenset()), int)
)

range_slice_ok = (
    hash(range(0, 3, 2)) == hash(range(0, 4, 2))
    and hash(slice(1, 2, None)) == hash(slice(1.0, 2, None))
    and isinstance(hash(slice(None, None, None)), int)
)

singleton_ok = isinstance(hash(None), int) and isinstance(hash(Ellipsis), int)

errors_ok = True

try:
    hash([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    hash({})
except TypeError:
    pass
else:
    errors_ok = False

try:
    hash(set())
except TypeError:
    pass
else:
    errors_ok = False

try:
    hash(bytearray(b"abc"))
except TypeError:
    pass
else:
    errors_ok = False

try:
    hash(([],))
except TypeError:
    pass
else:
    errors_ok = False

try:
    hash(slice([], None, None))
except TypeError:
    pass
else:
    errors_ok = False

result = (
    integer_ok
    and numeric_equality_ok
    and string_bytes_ok
    and tuple_ok
    and frozenset_ok
    and range_slice_ok
    and singleton_ok
    and errors_ok
)
assert result
result
