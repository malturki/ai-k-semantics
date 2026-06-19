result = int() == 0 and int(False) == 0 and int(True) == 1
result = result and int(7) == 7 and int(-3) == -3
result = result and bool(int(False)) is False and bool(int(True)) is True
assert result
result
