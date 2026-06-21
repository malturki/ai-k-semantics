result = int(b"123") == 123
result = result and int(b"   -12_345\n") == -12345
result = result and int(b"+101", 2) == 5
result = result and int(b"0b1_010", 0) == 10
result = result and int(b"0xFf", 16) == 255
result = result and int(b"\t+0o17\r", 0) == 15
assert result
result
