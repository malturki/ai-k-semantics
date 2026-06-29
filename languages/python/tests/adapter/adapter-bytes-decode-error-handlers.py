bad_utf8 = b"\xffa\xc3(b"
truncated3 = b"\xe2\x82"
truncated4 = b"\xf0\x9f\x98"
prefix_invalid = b"\xe2\x82("
overlong = b"\xc0\xaf"
bad_ascii = b"a\x80b\xff"

result = bad_utf8.decode("utf-8", "ignore") == "a(b"
result = result and bad_utf8.decode("utf-8", "replace") == "\ufffda\ufffd(b"
result = result and truncated3.decode("utf-8", "ignore") == ""
result = result and truncated3.decode("utf-8", "replace") == "\ufffd"
result = result and truncated4.decode("utf-8", "ignore") == ""
result = result and truncated4.decode("utf-8", "replace") == "\ufffd"
result = result and prefix_invalid.decode("utf-8", "ignore") == "("
result = result and prefix_invalid.decode("utf-8", "replace") == "\ufffd("
result = result and overlong.decode("utf-8", "ignore") == ""
result = result and overlong.decode("utf-8", "replace") == "\ufffd\ufffd"
result = result and bad_ascii.decode("ascii", "ignore") == "ab"
result = result and bad_ascii.decode("ascii", "replace") == "a\ufffdb\ufffd"

assert result
result
