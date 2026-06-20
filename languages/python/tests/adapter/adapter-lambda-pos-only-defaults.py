seed = 2

only = lambda x=seed, /: x == 2
only_override = lambda x=seed, /: x == 5
combined = lambda x, y=seed, /, z=3, w=4: x * 1000 + y * 100 + z * 10 + w
rest_keywords = lambda x=1, /, y=2, z=3: x == 1 and y == 6 and z == 3

seed = 99
result = only()
result = result and only_override(5)
result = result and combined(1) == 1234
result = result and combined(1, 4) == 1434
result = result and combined(1, 4, 5) == 1454
result = result and combined(1, z=6, w=7) == 1267
result = result and combined(1, 4, w=8) == 1438
result = result and rest_keywords(y=6)
assert result
result
