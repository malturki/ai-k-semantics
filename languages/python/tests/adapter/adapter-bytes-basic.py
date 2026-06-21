data = b"abc"
empty = b""

result = bool(data) and not bool(empty)
result = result and len(data) == 3 and len(empty) == 0
result = result and data == b"abc" and data != b"abd" and data != "abc"
result = result and data[0] == 97 and data[-1] == 99
result = result and data[1:3] == b"bc"
result = result and data[:2] == b"ab"
result = result and data[::-1] == b"cba"
result = result and 97 in data and 100 not in data
result = result and b"ab" + b"c" == data
result = result and b"a" * 3 == b"aaa" and b"a" * 0 == b""
result = result and list(data) == [97, 98, 99]
result = result and tuple(data) == (97, 98, 99)

assert result
result
