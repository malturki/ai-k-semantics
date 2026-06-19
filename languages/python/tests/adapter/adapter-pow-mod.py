result = pow(2, 5, 7) == 4
result = result and pow(-2, 3, 5) == 2
result = result and pow(2, 0, 3) == 1
result = result and pow(True, 5, 2) == 1
result = result and pow(2, 3, -5) == -2
assert result
result
