utf8_latin = bytearray(b"caf\xc3\xa9")
utf8_euro = bytearray(b"\xe2\x82\xac")
latin1_data = bytearray(b"\xff\xe9")
empty = bytearray()

decoded = utf8_latin.decode()

result = decoded == "caf\xe9"
result = result and isinstance(decoded, str)
result = result and utf8_euro.decode("utf-8") == "\u20ac"
result = result and latin1_data.decode("latin-1") == "\xff\xe9"
result = result and empty.decode() == ""
result = result and utf8_latin == bytearray(b"caf\xc3\xa9")

assert result
result
