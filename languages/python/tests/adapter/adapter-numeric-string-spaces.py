result = int(" 123 ") == 123
result = result and int(" -42 ") == -42
result = result and int(" +7 ", 10) == 7
result = result and float(" 1.5 ") == 1.5
result = result and float(" -2.5e-1 ") == -0.25

assert result
result
