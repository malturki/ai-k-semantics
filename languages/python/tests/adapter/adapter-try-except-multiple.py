first = 0
try:
    raise TypeError
except ValueError:
    first = 10
except TypeError:
    first = 3
except TypeError:
    first = 99

second = 0
try:
    raise ValueError
except ValueError:
    second = 1
except ValueError:
    second = 2

third = 0
try:
    try:
        raise KeyError
    except ValueError:
        third = 10
    except TypeError:
        third = 20
except KeyError:
    third = 4

result = first == 3 and second == 1 and third == 4
assert result
result
