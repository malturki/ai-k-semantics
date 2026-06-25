result = (-2.0) ** 3 == -8.0
result = result and (-2.0) ** 4 == 16.0
result = result and (-2.0) ** -3 == -0.125
result = result and (-2.0) ** True == -2.0
result = result and (-2.0) ** False == 1.0

result = result and pow(-2.0, 3) == -8.0
result = result and pow(-2.0, 4) == 16.0
result = result and pow(-2.0, -3) == -0.125
result = result and pow(-2.0, True) == -2.0
result = result and pow(-2.0, False) == 1.0

assert result
result
