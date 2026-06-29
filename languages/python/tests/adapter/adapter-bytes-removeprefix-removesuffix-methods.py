data = b"banana"

removeprefix_ok = (
    data.removeprefix(b"ban") == b"ana"
    and data.removeprefix(b"ana") == b"banana"
    and data.removeprefix(b"banana") == b""
)

removesuffix_ok = (
    data.removesuffix(b"ana") == b"ban"
    and data.removesuffix(b"ban") == b"banana"
    and data.removesuffix(b"banana") == b""
)

result = removeprefix_ok and removesuffix_ok and data == b"banana"
assert result
result
