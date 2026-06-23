result = min(3.5, 1.25, 2.0) == 1.25
result = result and max(3.5, 1.25, 2.0) == 3.5
result = result and min(True, 0.5, False) == False
result = result and max(False, 2.5, True) == 2.5

result = result and min(1, 1.0) == 1
result = result and max(1, 1.0) == 1
result = result and min(2.0, 1, 1.5, key=None) == 1
result = result and max(False, 1.5, True, key=None) == 1.5

assert result
result
