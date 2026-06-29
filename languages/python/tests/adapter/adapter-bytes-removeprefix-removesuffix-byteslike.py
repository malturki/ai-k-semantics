data = b"banana"
empty = b""

byteslike_ok = (
    data.removeprefix(bytearray(b"ban")) == b"ana"
    and data.removeprefix(memoryview(b"ban")) == b"ana"
    and data.removesuffix(bytearray(b"ana")) == b"ban"
    and data.removesuffix(memoryview(b"ana")) == b"ban"
)

empty_affix_ok = (
    data.removeprefix(b"") == b"banana"
    and data.removesuffix(b"") == b"banana"
    and empty.removeprefix(b"") == b""
    and empty.removeprefix(b"x") == b""
    and empty.removesuffix(b"") == b""
    and empty.removesuffix(b"x") == b""
)

result = byteslike_ok and empty_affix_ok and data == b"banana" and empty == b""
assert result
result
