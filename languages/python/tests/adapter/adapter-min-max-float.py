result = min([2.5, 1.5, 3.0]) == 1.5
result = result and max([2.5, 1.5, 3.0]) == 3.0
result = result and min((1, 2.5, False)) == False
result = result and max((1.0, 2, False)) == 2

result = result and min([True, 0.5], default=99.0) == 0.5
result = result and max((False, -1.25), default=-99.0) == False
result = result and min([2.5, 1.5], key=None) == 1.5
result = result and max((1.0, 2.5), key=None, default=-1.0) == 2.5

assert result
result
