result = divmod(7, 3) == (2, 1)
result = result and divmod(-7, 3) == (-3, 2)
result = result and divmod(7, -3) == (-3, -2)
result = result and divmod(True, True) == (1, 0)
result = result and divmod(False, True) == (0, 0)
assert result
result
