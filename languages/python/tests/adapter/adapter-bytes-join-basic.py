dash = b"-"
empty = b""
wide = b"--"

empty_iterable_ok = (
    dash.join([]) == b""
    and empty.join([]) == b""
)

single_ok = (
    dash.join([b"a"]) == b"a"
    and wide.join((b"abc",)) == b"abc"
)

multi_ok = (
    dash.join([b"a", b"b", b"c"]) == b"a-b-c"
    and empty.join([b"a", b"b", b"c"]) == b"abc"
    and wide.join((b"a", b"b", b"c")) == b"a--b--c"
    and empty.join([b"", b"a", b""]) == b"a"
)

unchanged_ok = dash == b"-" and empty == b"" and wide == b"--"

result = empty_iterable_ok and single_ok and multi_ok and unchanged_ok
assert result
result
