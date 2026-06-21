result = float("0") == 0.0
result = result and float("123") == 123.0
result = result and float("-42") == -42.0
result = result and float("+7") == 7.0

assert result
result
