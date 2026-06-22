result = 0
try:
    result = 1
    raise ValueError
    result = 2
except ValueError:
    result = result + 3
result = result == 4
assert result
result
