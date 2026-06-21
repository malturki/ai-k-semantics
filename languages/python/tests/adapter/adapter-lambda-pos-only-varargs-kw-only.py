seed = 5

collect = lambda x, /, y, *args, z: x * 100000 + y * 10000 + z * 1000 + len(args) * 100 + (args[0] if len(args) else 0)
defaults = lambda x=seed, /, y=4, *args, z=6, w=8: x * 100000 + y * 10000 + z * 1000 + w * 100 + len(args) * 10 + (args[0] if len(args) else 0)

seed = 99

result = collect(1, 2, z=3) == 123000
result = result and collect(1, 2, 4, 5, z=3) == 123204
result = result and collect(1, y=2, z=3) == 123000
result = result and defaults(z=9) == 549800
result = result and defaults(9, 8, 6, 5, z=4, w=1) == 984126

assert result
result
