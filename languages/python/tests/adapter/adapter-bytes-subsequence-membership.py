data = b"abracadabra"
empty = b""

result = b"" in empty and b"" in data
result = result and b"a" in data and b"abra" in data
result = result and b"cad" in data and b"dab" in data
result = result and b"ra" in data and b"bra" in data
result = result and b"abc" not in data and b"abracadabraa" not in data
result = result and b"a" not in empty
result = result and (b"abra" in data in [data])
result = result and (b"zz" not in data in [data])
result = result and (b"" in empty in [empty])
result = result and (b"a" not in empty in [empty])

assert result
result
