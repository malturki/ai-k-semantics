result = pow(2, 3) == 8
result = result and pow(-2, 3) == -8
result = result and pow(5, 0) == 1
result = result and pow(True, 5) == 1
result = result and pow(False, True) == 0
result = result and pow(2, False) == 1
assert result
result
