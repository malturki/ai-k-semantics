a = 9
result = min(3, 1, 2) == 1
result = result and max(3, 1, 2) == 3
result = result and min(True, 2, False) == False
result = result and max(False, 2, True) == 2
result = result and min(a - 4, 10 // 2, 7) == 5
result = result and max(a - 4, 10 // 2, 7) == 7
assert result
result
