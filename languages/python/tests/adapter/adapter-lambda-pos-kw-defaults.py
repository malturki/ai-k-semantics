seed = 2
combine = lambda x, y=seed, *, scale, offset=1: (x + y) * scale + offset
seed = 99

result = combine(3, scale=4) == 21
result = result and combine(3, 4, scale=5, offset=6) == 41
result = result and combine(x=3, scale=4) == 21
result = result and combine(3, y=4, scale=5) == 36

just = lambda x, *, y=5: x + y
result = result and just(7) == 12
assert result
result
