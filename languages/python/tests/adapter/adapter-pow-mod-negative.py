result = pow(3, -1, 11) == 4
result = result and pow(3, -2, 11) == 5
result = result and pow(2, -3, 5) == 2
result = result and pow(-3, -1, 11) == 7
result = result and pow(3, -1, -11) == -7
result = result and pow(-3, -1, -11) == -4
result = result and pow(2, -3, -5) == -3
result = result and pow(10, -1, 17) == 12
result = result and pow(True, -1, 2) == 1
result = result and pow(2, -1, 1) == 0
assert result
result
