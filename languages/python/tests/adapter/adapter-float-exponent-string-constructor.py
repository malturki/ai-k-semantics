result = float("1e3") == 1000.0
result = result and float("1.5e2") == 150.0
result = result and float("-2.5e-1") == -0.25
result = result and float("+3E+2") == 300.0
result = result and float(".5e1") == 5.0

assert result
result
