result = float("1.5") == 1.5
result = result and float("-0.25") == -0.25
result = result and float("+12.0") == 12.0
result = result and float(".5") == 0.5
result = result and float("5.") == 5.0

assert result
result
