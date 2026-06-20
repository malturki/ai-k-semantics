result = 1.5 + 2.25 == 3.75
result = result and 5.0 - 2 == 3.0
result = result and 2 * 1.5 == 3.0
result = result and 7.5 / 2.5 == 3.0
result = result and 3 / 2.0 == 1.5
result = result and +1.5 == 1.5 and -1.5 == -1.5
result = result and abs(-1.25) == 1.25 and abs(0.0) == 0.0
result = result and 1 < 1.5 and 2.0 >= True
result = result and False <= 0.0 and 2.5 > 2
result = result and 1.0 == True and 0.0 == False and 1.0 != False
assert result
result
