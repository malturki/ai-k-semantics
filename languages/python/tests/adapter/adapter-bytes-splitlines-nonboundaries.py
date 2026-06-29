not_boundaries = b"a\x0b b\x0c c"

result = not_boundaries.splitlines() == [b"a\x0b b\x0c c"]
assert result
result
