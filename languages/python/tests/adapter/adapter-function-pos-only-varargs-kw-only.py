seed = 4

def collect(x, /, y, *args, z):
    return x * 100000 + y * 10000 + z * 1000 + len(args) * 100 + (args[0] if len(args) else 0)

def defaults(x=seed, /, y=3, *args, z=5, w=7):
    return x * 100000 + y * 10000 + z * 1000 + w * 100 + len(args) * 10 + (args[0] if len(args) else 0)

seed = 99

result = collect(1, 2, z=3) == 123000
result = result and collect(1, 2, 4, 5, z=3) == 123204
result = result and collect(1, y=2, z=3) == 123000
result = result and defaults(z=8) == 438700
result = result and defaults(9, 8, 6, 5, z=4, w=1) == 984126

assert result
result
