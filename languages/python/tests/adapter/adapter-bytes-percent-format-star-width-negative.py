result = (b"%*b|%-*s" % (-5, b"xy", 5, b"uv")) == b"xy   |uv   "

assert result
result
