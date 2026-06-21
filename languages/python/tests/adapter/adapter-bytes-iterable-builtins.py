data = b"cab"
with_zero = b"\x01\x00"

result = all(b"\x01\x02")
result = result and not all(with_zero)
result = result and any(b"\x00\x03")
result = result and not any(b"")
result = result and sum(b"\x01\x02\x03") == 6
result = result and sum(b"\x01", 4) == 5
result = result and min(data) == 97 and max(data) == 99
result = result and [*b"ab"] == [97, 98]

assert result
result
