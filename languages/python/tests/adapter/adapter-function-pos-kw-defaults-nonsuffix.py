def choose(x, *, a=1, b, c=3):
    return x * 1000 + a * 100 + b * 10 + c

result = choose(9, b=2) == 9123
result = result and choose(9, a=4, b=5) == 9453
result = result and choose(9, b=6, c=7) == 9167
result = result and choose(9, a=8, b=9, c=1) == 9891
assert result
result
