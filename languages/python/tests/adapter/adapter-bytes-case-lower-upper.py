empty = b""
mixed = b"AbC123!"
non_ascii = b"\xffAbC"

result = (
    empty.lower() == b""
    and empty.upper() == b""
    and mixed.lower() == b"abc123!"
    and mixed.upper() == b"ABC123!"
    and non_ascii.lower() == b"\xffabc"
    and non_ascii.upper() == b"\xffABC"
    and mixed == b"AbC123!"
    and non_ascii == b"\xffAbC"
)

assert result
result
