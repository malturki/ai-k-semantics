result = 7 / 2 == 3.5
result = result and -7 / 2 == -3.5
result = result and 7 / -2 == -3.5
result = result and True / 2 == 0.5
result = result and False / 5 == 0.0
result = result and bool(1 / 2)
result = result and not bool(0 / 5)
assert result
result
