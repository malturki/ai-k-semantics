from_bytes = memoryview(b"abc")
from_bytearray = memoryview(bytearray(b"xy"))
from_empty = memoryview(b"")
from_high_bytes = memoryview(bytearray(b"\x00\xff"))

bytes_ok = (
    bytes(from_bytes) == b"abc"
    and bytes(from_bytearray) == b"xy"
    and bytes(from_empty) == b""
    and bytes(from_high_bytes) == b"\x00\xff"
)

bytearray_ok = (
    bytearray(from_bytes) == bytearray(b"abc")
    and bytearray(from_bytearray) == bytearray(b"xy")
    and bytearray(from_empty) == bytearray(b"")
    and bytearray(from_high_bytes) == bytearray(b"\x00\xff")
)

cross_ok = (
    bytes(memoryview(bytearray(bytes(from_bytes)))) == b"abc"
    and bytearray(memoryview(bytes(from_bytearray))) == bytearray(b"xy")
)

result = bytes_ok and bytearray_ok and cross_ok
assert result
result
