result = int("1_000") == 1000
result = result and int("-1_2") == -12
result = result and int("ff_ff", 16) == 65535
result = result and int(" 1_2 ") == 12
result = result and float("1_000") == 1000.0

assert result
result
