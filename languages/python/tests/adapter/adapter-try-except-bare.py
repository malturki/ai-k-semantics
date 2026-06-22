first = 0
try:
    raise ValueError
except:
    first = 1

second = 0
try:
    raise TypeError
except ValueError:
    second = 10
except:
    second = 2

normal = 0
try:
    normal = normal + 1
except:
    normal = normal + 10
else:
    normal = normal + 100

handled = 0
try:
    raise KeyError
except ValueError:
    handled = handled + 10
except:
    handled = handled + 3
else:
    handled = handled + 30

result = first == 1 and second == 2 and normal == 101 and handled == 3
assert result
result
