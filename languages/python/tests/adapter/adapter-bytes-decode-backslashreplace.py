bad_utf8 = b"\xffa\xc3(b"
truncated = b"\xf0\x9f\x98"
prefix_invalid = b"\xe2\x82("
overlong = b"\xc0\xaf"
bad_ascii = b"a\x80b\xff"

result = bad_utf8.decode("utf-8", "backslashreplace") == "\\xffa\\xc3(b"
result = result and truncated.decode("utf-8", "backslashreplace") == "\\xf0\\x9f\\x98"
result = result and prefix_invalid.decode("utf-8", "backslashreplace") == "\\xe2\\x82("
result = result and overlong.decode("utf-8", "backslashreplace") == "\\xc0\\xaf"
result = result and bad_ascii.decode("ascii", "backslashreplace") == "a\\x80b\\xff"

assert result
result
