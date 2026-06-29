bad_utf8 = bytearray(b"\xffa\xc3(b")
truncated = bytearray(b"\xf0\x9f\x98")
bad_ascii = bytearray(b"a\x80b\xff")
latin1_data = bytearray(b"\xff\xe9")

result = bad_utf8.decode("utf8", "backslashreplace") == "\\xffa\\xc3(b"
result = result and truncated.decode("utf-8", "backslashreplace") == "\\xf0\\x9f\\x98"
result = result and bad_ascii.decode("ascii", "backslashreplace") == "a\\x80b\\xff"
result = result and latin1_data.decode("latin-1", "backslashreplace") == "\xff\xe9"
result = result and isinstance(bad_utf8.decode("utf-8", "backslashreplace"), str)

assert result
result
