empty = b""
mixed = b"AbC123!"
number_prefix = b"123ABC"
word_digits = b"a1b"
phrase = b"hello world"
apostrophe = b"they're bill's"
non_ascii = b"\xffAbC"

result = (
    empty.title() == b""
    and mixed.title() == b"Abc123!"
    and number_prefix.title() == b"123Abc"
    and word_digits.title() == b"A1B"
    and phrase.title() == b"Hello World"
    and apostrophe.title() == b"They'Re Bill'S"
    and non_ascii.title() == b"\xffAbc"
    and mixed == b"AbC123!"
    and apostrophe == b"they're bill's"
)

assert result
result
