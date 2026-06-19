values = range(1, 8, 2)
descending = range(6, 0, -2)
empty = range(5, 2)

result = 1 in values and 3 in values and 2 not in values and True in range(3) and False in range(0, 1) and 4 in descending and 5 not in descending and 3 not in empty
assert result
result
