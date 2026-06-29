empty = bytearray()
edge = bytearray(b",a,")

explicit_ok = (
    empty.split(b",") == [bytearray()]
    and edge.split(b",") == [bytearray(), bytearray(b"a"), bytearray()]
)

unchanged_ok = (
    empty == bytearray()
    and edge == bytearray(b",a,")
)

result = explicit_ok and unchanged_ok
assert result
result
