mix = lambda x, /, y: x * 10 + y
only = lambda x, /: x + 1

result = mix(2, 3) == 23
result = result and mix(2, y=4) == 24
result = result and only(5) == 6
assert result
result
