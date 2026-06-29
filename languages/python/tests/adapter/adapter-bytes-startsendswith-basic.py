data = b"banana"
empty = b""

result = (
    data.startswith(b"ban")
    and not data.startswith(b"ana")
    and data.startswith(bytearray(b"ban"))
    and data.startswith(memoryview(b"ban"))
    and data.startswith(b"")
    and empty.startswith(b"")
    and not empty.startswith(b"x")
    and data.endswith(b"ana")
    and not data.endswith(b"ban")
    and data.endswith(bytearray(b"ana"))
    and data.endswith(memoryview(b"ana"))
    and data.endswith(b"")
    and empty.endswith(b"")
    and not empty.endswith(b"x")
)

assert result
result
