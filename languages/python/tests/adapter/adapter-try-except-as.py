single = False
continued = 0
try:
    raise ValueError
except ValueError as err:
    single = err == err
    continued = continued + 1
continued = continued + 1

multi = False
try:
    raise TypeError
except ValueError as err:
    multi = False
except TypeError as err:
    multi = err == err

result = single and continued == 2 and multi
assert result
result
