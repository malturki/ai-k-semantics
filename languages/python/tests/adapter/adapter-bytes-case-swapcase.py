empty = b""
mixed = b"AbC123!"
number_prefix = b"123ABC"
word_digits = b"a1b"
apostrophe = b"they're bill's"
non_ascii = b"\xffAbC"

result = (
    empty.swapcase() == b""
    and mixed.swapcase() == b"aBc123!"
    and number_prefix.swapcase() == b"123abc"
    and word_digits.swapcase() == b"A1B"
    and apostrophe.swapcase() == b"THEY'RE BILL'S"
    and non_ascii.swapcase() == b"\xffaBc"
    and mixed == b"AbC123!"
    and apostrophe == b"they're bill's"
)

assert result
result
