seed = 5

def mix(x, /, y, *, z):
    return x * 100 + y * 10 + z

def defaults(x=seed, /, y=3, *, z=4, w=1):
    return x * 1000 + y * 100 + z * 10 + w

seed = 99

result = mix(1, 2, z=3) == 123
result = result and mix(1, y=2, z=3) == 123
result = result and defaults() == 5341
result = result and defaults(y=6) == 5641
result = result and defaults(7, z=8) == 7381
result = result and defaults(7, y=6, z=8, w=9) == 7689

assert result
result
