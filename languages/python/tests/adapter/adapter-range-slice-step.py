r = range(2, 14, 2)
descending = range(9, -3, -3)

result = r[1:5:2] == range(4, 12, 4) and r[::-1] == range(12, 0, -2) and r[5:1:-2] == range(12, 4, -4) and r[::3] == range(2, 14, 6) and descending[::2] == range(9, -3, -6) and descending[::-1] == range(0, 12, 3) and descending[3:0:-1] == range(0, 9, 3)
assert result
result
