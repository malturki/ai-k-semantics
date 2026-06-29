empty = b""
alpha = b"ABCabc"
alnum = b"ABCabc123"
digits = b"0123456789"
lower = b"abc123!"
lower_punct = b"abc!"

result = (
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

assert result
result
