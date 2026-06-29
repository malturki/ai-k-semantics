ascii_data = b"spam"
utf8_latin = b"caf\xc3\xa9"
utf8_omega = b"\xce\xa9"
utf8_euro = b"\xe2\x82\xac"
utf8_face = b"\xf0\x9f\x98\x80"
empty = b""

result = ascii_data.decode() == "spam"
result = result and utf8_latin.decode() == "caf\xe9"
result = result and utf8_omega.decode("utf8") == "\u03a9"
result = result and utf8_euro.decode("UTF-8") == "\u20ac"
result = result and utf8_face.decode() == "\U0001f600"
result = result and empty.decode() == ""
result = result and ascii_data.decode("utf-8", "made-up-handler") == "spam"

assert result
result
