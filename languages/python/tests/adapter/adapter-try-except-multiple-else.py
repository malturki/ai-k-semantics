normal = 0
try:
    normal = normal + 1
except ValueError:
    normal = normal + 10
except TypeError:
    normal = normal + 20
else:
    normal = normal + 100

handled = 0
try:
    raise TypeError
except ValueError:
    handled = handled + 10
except TypeError:
    handled = handled + 2
else:
    handled = handled + 30

result = normal == 101 and handled == 2
assert result
result
