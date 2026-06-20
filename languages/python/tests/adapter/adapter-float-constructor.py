result = float() == 0.0
result = result and float(7) == 7.0 and float(-3) == -3.0
result = result and float(True) == 1.0 and float(False) == 0.0
result = result and float(1.25) == 1.25
result = result and bool(float(0)) is False and bool(float(True)) is True
assert result
result
