empty = bytearray()
mixed = bytearray(b"AbC123!")
number_prefix = bytearray(b"123ABC")
word_digits = bytearray(b"a1b")
phrase = bytearray(b"hello world")
apostrophe = bytearray(b"they're bill's")
non_ascii = bytearray(b"\xffAbC")

lower_upper_ok = (
    empty.lower() == bytearray()
    and empty.upper() == bytearray()
    and mixed.lower() == bytearray(b"abc123!")
    and mixed.upper() == bytearray(b"ABC123!")
    and non_ascii.lower() == bytearray(b"\xffabc")
    and non_ascii.upper() == bytearray(b"\xffABC")
)

capitalize_ok = (
    empty.capitalize() == bytearray()
    and mixed.capitalize() == bytearray(b"Abc123!")
    and number_prefix.capitalize() == bytearray(b"123abc")
    and word_digits.capitalize() == bytearray(b"A1b")
    and non_ascii.capitalize() == bytearray(b"\xffabc")
)

swapcase_ok = (
    empty.swapcase() == bytearray()
    and mixed.swapcase() == bytearray(b"aBc123!")
    and number_prefix.swapcase() == bytearray(b"123abc")
    and word_digits.swapcase() == bytearray(b"A1B")
    and apostrophe.swapcase() == bytearray(b"THEY'RE BILL'S")
    and non_ascii.swapcase() == bytearray(b"\xffaBc")
)

title_ok = (
    empty.title() == bytearray()
    and mixed.title() == bytearray(b"Abc123!")
    and number_prefix.title() == bytearray(b"123Abc")
    and word_digits.title() == bytearray(b"A1B")
    and phrase.title() == bytearray(b"Hello World")
    and apostrophe.title() == bytearray(b"They'Re Bill'S")
    and non_ascii.title() == bytearray(b"\xffAbc")
)

unchanged_ok = (
    mixed == bytearray(b"AbC123!")
    and apostrophe == bytearray(b"they're bill's")
    and non_ascii == bytearray(b"\xffAbC")
)

result = lower_upper_ok and capitalize_ok and swapcase_ok and title_ok and unchanged_ok
assert result
result
