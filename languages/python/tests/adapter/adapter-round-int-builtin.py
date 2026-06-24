result = round(0) == 0
result = result and round(8) == 8
result = result and round(-8) == -8
result = result and round(True) == 1
result = result and round(False) == 0
result = result and round(123, None) == 123
result = result and round(123, 2) == 123
result = result and round(123, 0) == 123
result = result and round(-8, 1) == -8
result = result and round(-8, 0) == -8
result = result and round(True, -1) == 0

result = result and round(123, -1) == 120
result = result and round(128, -1) == 130
result = result and round(-123, -1) == -120
result = result and round(-128, -1) == -130

result = result and round(125, -1) == 120
result = result and round(135, -1) == 140
result = result and round(-125, -1) == -120
result = result and round(-135, -1) == -140
result = result and round(150, -2) == 200
result = result and round(250, -2) == 200

assert result
result
