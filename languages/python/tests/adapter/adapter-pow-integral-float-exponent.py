result = (-9.0) ** 2.0 == 81.0
result = result and (-2.0) ** -3.0 == -0.125
result = result and (-2.0) ** 0.0 == 1.0
result = result and (-3) ** 2.0 == 9.0
result = result and (-2) ** -3.0 == -0.125
result = result and (-2) ** 0.0 == 1.0

result = result and pow(-9.0, 2.0) == 81.0
result = result and pow(-2.0, -3.0) == -0.125
result = result and pow(-2.0, 0.0) == 1.0
result = result and pow(-3, 2.0) == 9.0
result = result and pow(-2, -3.0) == -0.125
result = result and pow(-2, 0.0) == 1.0

assert result
result
