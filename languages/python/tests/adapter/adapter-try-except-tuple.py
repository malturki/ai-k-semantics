first = 0
try:
    raise TypeError
except (ValueError, TypeError):
    first = 1

second = 0
try:
    raise KeyError
except (ValueError, TypeError):
    second = 10
except KeyError:
    second = 2

third = False
try:
    raise ValueError
except (ValueError, TypeError) as err:
    third = err == err

normal = 0
try:
    normal = normal + 1
except (ValueError, TypeError):
    normal = normal + 10
else:
    normal = normal + 100

result = first == 1 and second == 2 and third and normal == 101
assert result
result
