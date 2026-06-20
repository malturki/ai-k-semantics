result = 7.5 // 2.0 == 3.0 and 7.5 % 2.0 == 1.5
result = result and divmod(7.5, 2.0) == (3.0, 1.5)
result = result and -7.5 // 2.0 == -4.0 and -7.5 % 2.0 == 0.5
result = result and 7.5 // -2.0 == -4.0 and 7.5 % -2.0 == -0.5
result = result and 5 // 2.0 == 2.0 and 5 % 2.0 == 1.0
result = result and 5.0 // True == 5.0 and 5.0 % True == 0.0
assert result
result
