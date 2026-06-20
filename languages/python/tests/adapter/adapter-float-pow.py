result = 2.0 ** 3.0 == 8.0 and 4.0 ** 0.5 == 2.0
result = result and 2.0 ** -2 == 0.25
result = result and 2 ** 3.0 == 8.0 and True ** 2.0 == 1.0
result = result and pow(9.0, 0.5) == 3.0 and pow(2, -2.0) == 0.25
assert result
result
