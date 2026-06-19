result = abs(0) == 0 and abs(5) == 5 and abs(-5) == 5
result = result and abs(True) == 1 and abs(False) == 0
result = result and bool(abs(False)) is False and bool(abs(True)) is True
assert result
result
