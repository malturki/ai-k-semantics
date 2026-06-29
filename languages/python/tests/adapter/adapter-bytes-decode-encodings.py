ascii_data = b"AZaz09"
latin1_data = b"\xff\xe9"
ascii_array = bytearray(ascii_data)

result = ascii_data.decode("ascii") == "AZaz09"
result = result and ascii_data.decode("ASCII", "strict") == "AZaz09"
result = result and latin1_data.decode("latin-1") == "\xff\xe9"
result = result and latin1_data.decode("latin_1") == "\xff\xe9"
result = result and latin1_data.decode("iso-8859-1") == "\xff\xe9"
result = result and ascii_array.decode("ascii") == "AZaz09"

assert result
result
