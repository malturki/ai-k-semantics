combine = lambda x, y, *, scale, offset: (x + y) * scale + offset

result = combine(2, 3, scale=4, offset=1) == 21
result = result and combine(2, y=3, scale=4, offset=1) == 21
result = result and combine(x=2, y=3, scale=4, offset=1) == 21
assert result
result
