seed = 6

mix = lambda x, /, y, *, z: x * 100 + y * 10 + z
defaults = lambda x=seed, /, y=4, *, z=5, w=2: x * 1000 + y * 100 + z * 10 + w

seed = 99

result = mix(1, 2, z=3) == 123
result = result and mix(1, y=2, z=3) == 123
result = result and defaults() == 6452
result = result and defaults(y=7) == 6752
result = result and defaults(8, z=9) == 8492
result = result and defaults(8, y=7, z=9, w=1) == 8791

assert result
result
