result = round(0.0) == 0
result = result and round(1.0) == 1
result = result and round(-1.0) == -1
result = result and round(0.1) == 0
result = result and round(0.9) == 1
result = result and round(-0.1) == 0
result = result and round(-0.9) == -1

result = result and round(5.5) == 6
result = result and round(6.5) == 6
result = result and round(-5.5) == -6
result = result and round(-6.5) == -6

result = result and round(1234.56, None) == 1235
result = result and round(-1234.56, None) == -1235

result = result and round(1.25, 1) == 1.2
result = result and round(1.75, 1) == 1.8
result = result and round(0.125, 2) == 0.12
result = result and round(0.375, 2) == 0.38
result = result and round(-8.0, -1) == -10.0
result = result and round(15.0, -1) == 20.0
result = result and round(25.0, -1) == 20.0

assert result
result
