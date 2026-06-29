empty = b""
mixed = b"AbC123!"
number_prefix = b"123ABC"
word_digits = b"a1b"
non_ascii = b"\xffAbC"

result = (
    empty.capitalize() == b""
    and mixed.capitalize() == b"Abc123!"
    and number_prefix.capitalize() == b"123abc"
    and word_digits.capitalize() == b"A1b"
    and non_ascii.capitalize() == b"\xffabc"
    and mixed == b"AbC123!"
    and non_ascii == b"\xffAbC"
)

assert result
result
