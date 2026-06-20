result = 1.0 in range(3)
result = result and not (1.5 in range(3))
result = result and 2.0 in range(5, 0, -1)
result = result and not (2.5 in range(5, 0, -1))
result = result and not ("1" in range(3))
result = result and not (None in range(3))

assert result
result
