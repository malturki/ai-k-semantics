result = 2 ** -3 == 0.125
result = result and (-2) ** -3 == -0.125
result = result and (-2) ** -2 == 0.25
result = result and pow(4, -2) == 0.0625
result = result and True ** -1 == 1.0
assert result
result
