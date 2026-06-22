first = 0
try:
    first = first + 1
except ValueError:
    first = first + 10
else:
    first = first + 100

second = 0
try:
    raise ValueError
except ValueError:
    second = second + 3
else:
    second = second + 30

result = first == 101 and second == 3
assert result
result
