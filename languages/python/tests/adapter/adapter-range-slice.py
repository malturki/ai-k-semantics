r = range(2, 10, 2)
descending = range(9, 1, -3)

result = r[1:3] == range(4, 8, 2) and r[:2] == range(2, 6, 2) and r[2:] == range(6, 10, 2) and r[-3:-1] == range(4, 8, 2) and r[3:1] == range(0) and descending[1:] == range(6, 0, -3) and descending[:2] == range(9, 3, -3) and descending[-2:] == range(6, 0, -3)
assert result
result
