empty = bytearray()
lower = bytearray(b"abc123!")
upper = bytearray(b"ABC123!")
alpha = bytearray(b"ABCabc")
alnum = bytearray(b"ABCabc123")
digits = bytearray(b"0123456789")
spaces = bytearray(b" \t\n\r\v\f")
one_space = bytearray(b" ")
lower_punct = bytearray(b"abc!")
upper_punct = bytearray(b"ABC!")
title = bytearray(b"Abc Def")
title_with_digits = bytearray(b"A1B")
all_lower = bytearray(b"abc")
all_upper = bytearray(b"ABC")
not_title_lower_start = bytearray(b"1a")
not_title_lower_word = bytearray(b"Abc def")
non_ascii = bytearray(b"\x00\x7f\x80\xff")

ascii_ok = (
    empty.isascii()
    and lower.isascii()
    and spaces.isascii()
    and not non_ascii.isascii()
)

alpha_digit_alnum_ok = (
    alpha.isalpha()
    and not empty.isalpha()
    and not alnum.isalpha()
    and digits.isdigit()
    and not empty.isdigit()
    and not lower.isdigit()
    and alnum.isalnum()
    and digits.isalnum()
    and not empty.isalnum()
    and not lower_punct.isalnum()
)

case_ok = (
    lower.islower()
    and lower_punct.islower()
    and not empty.islower()
    and not upper.islower()
    and not digits.islower()
    and upper.isupper()
    and upper_punct.isupper()
    and not empty.isupper()
    and not lower.isupper()
    and not digits.isupper()
)

space_title_ok = (
    spaces.isspace()
    and one_space.isspace()
    and not empty.isspace()
    and not lower.isspace()
    and title.istitle()
    and title_with_digits.istitle()
    and not empty.istitle()
    and not all_lower.istitle()
    and not all_upper.istitle()
    and not not_title_lower_start.istitle()
    and not not_title_lower_word.istitle()
)

unchanged_ok = (
    lower == bytearray(b"abc123!")
    and upper == bytearray(b"ABC123!")
    and non_ascii == bytearray(b"\x00\x7f\x80\xff")
)

result = ascii_ok and alpha_digit_alnum_ok and case_ok and space_title_ok and unchanged_ok
assert result
result
