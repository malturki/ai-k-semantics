result = int("0b101", 0) == 5
result = result and int("0o77", 0) == 63
result = result and int("0xFF", 0) == 255
result = result and int("+0x10", 0) == 16
result = result and int("-0b101", 0) == -5
result = result and int(" 0x_f ", 0) == 15
result = result and int("0b101", 2) == 5
result = result and int("0o77", 8) == 63
result = result and int("0x_FF", 16) == 255
result = result and int("1_000", 0) == 1000
result = result and int("0_0", 0) == 0

assert result
result
