data = b"banana"

result = (
    data.startswith((b"ban", 1))
    and data.startswith((b"",))
    and data.startswith((memoryview(b"ban"),))
    and not data.startswith(())
    and data.endswith((b"ana", 1))
    and data.endswith((b"",))
    and data.endswith((memoryview(b"ana"),))
    and not data.endswith(())
)

assert result
result
