result = 0
try:
    try:
        raise TypeError
    except ValueError:
        result = 10
except TypeError:
    result = result + 3
result = result == 3
assert result
result
