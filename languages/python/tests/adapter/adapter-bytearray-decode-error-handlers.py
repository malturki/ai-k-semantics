bad_utf8 = bytearray(b"\xffa\xc3(b")
truncated = bytearray(b"\xf0\x9f\x98")
bad_ascii = bytearray(b"a\x80b\xff")
latin1_data = bytearray(b"\xff\xe9")

result = bad_utf8.decode("utf8", "ignore") == "a(b"
result = result and bad_utf8.decode("utf8", "replace") == "\ufffda\ufffd(b"
result = result and truncated.decode("utf-8", "ignore") == ""
result = result and truncated.decode("utf-8", "replace") == "\ufffd"
result = result and bad_ascii.decode("ascii", "ignore") == "ab"
result = result and bad_ascii.decode("ascii", "replace") == "a\ufffdb\ufffd"
result = result and latin1_data.decode("latin-1", "ignore") == "\xff\xe9"
result = result and latin1_data.decode("latin-1", "replace") == "\xff\xe9"
result = result and isinstance(bad_utf8.decode("utf-8", "replace"), str)

assert result
result
