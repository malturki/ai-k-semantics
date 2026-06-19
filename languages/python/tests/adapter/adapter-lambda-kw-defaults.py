choose = lambda *, a, b=2: a * 10 + b
result = choose(a=1) == 12
result = result and choose(a=1, b=3) == 13
assert result
result
