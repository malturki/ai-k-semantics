empty = b""
lower = b"abc123!"
upper = b"ABC123!"
digits = b"123"
lower_punct = b"abc!"
upper_punct = b"ABC!"

result = (
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

assert result
result
