result = 0
try:
    result = 1
except ValueError:
    result = 2
result = result == 1
assert result
result
