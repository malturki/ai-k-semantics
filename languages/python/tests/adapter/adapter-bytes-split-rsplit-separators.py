empty = b""
edge = b",a,"

explicit_ok = (
    empty.split(b",") == [b""]
    and edge.split(b",") == [b"", b"a", b""]
)

result = explicit_ok and empty == b"" and edge == b",a,"
assert result
result
