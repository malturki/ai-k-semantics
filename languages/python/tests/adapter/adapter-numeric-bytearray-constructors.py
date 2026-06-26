result = int(bytearray(b"123")) == 123
result = result and int(bytearray(b"   -12_345\n")) == -12345
result = result and int(bytearray(b"+101"), 2) == 5
result = result and int(bytearray(b"0b1_010"), 0) == 10
result = result and int(bytearray(b"0xFf"), 16) == 255
result = result and int(bytearray(b"\t+0o17\r"), 0) == 15
result = result and float(bytearray(b"  -1.25\n")) == -1.25
result = result and float(bytearray(b"+1_2.5_0e+1")) == 125.0
result = result and float(bytearray(b"Infinity")) == float("inf")
result = result and float(bytearray(b"-inf")) == float("-Infinity")
nan_value = float(bytearray(b"nan"))
result = result and nan_value != nan_value
assert result
result
