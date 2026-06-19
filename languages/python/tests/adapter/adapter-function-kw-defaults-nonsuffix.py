def choose(*, a=1, b, c=3):
    return a * 100 + b * 10 + c

result = choose(b=2) == 123
result = result and choose(a=4, b=5) == 453
result = result and choose(b=6, c=7) == 167
result = result and choose(a=8, b=9, c=1) == 891
assert result
result
