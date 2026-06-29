bytes_value = bytes.fromhex(memoryview(b"2E f0"))
bytearray_value = bytearray.fromhex(bytearray(b"2E f0"))

result = (
    bytes_value == b".\xf0"
    and isinstance(bytes_value, bytes)
    and bytearray_value == bytearray(b".\xf0")
    and isinstance(bytearray_value, bytearray)
)
assert result
result
