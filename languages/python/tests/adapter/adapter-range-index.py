r = range(2, 10, 2)
descending = range(9, 1, -3)

result = r[0] == 2 and r[2] == 6 and r[-1] == 8 and r[True] == 4 and r[False] == 2 and descending[0] == 9 and descending[1] == 6 and descending[-1] == 3
assert result
result
