result = range(0) == range(2, 1, 3) and range(0, 3, 2) == range(0, 4, 2) and range(1, 8, 2) == range(1, 9, 2) and range(1, 8, 2) != range(1, 8, 3) and range(1, 2, 5) == range(1, 3, 5) and range(False, True) == range(1) and range(3) != range(4)
assert result
result
