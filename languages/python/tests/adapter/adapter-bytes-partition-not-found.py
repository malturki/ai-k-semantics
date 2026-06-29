plain = b"abc"
empty = b""

not_found_ok = (
    plain.partition(b":") == (b"abc", b"", b"")
    and plain.rpartition(b":") == (b"", b"", b"abc")
    and empty.partition(b"x") == (b"", b"", b"")
    and empty.rpartition(b"x") == (b"", b"", b"")
)

result = not_found_ok and plain == b"abc" and empty == b""
assert result
result
