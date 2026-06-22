first = 0
try:
    try:
        first = first + 1
        raise ValueError
    except ValueError:
        first = first + 2
    finally:
        first = first + 4
except TypeError:
    first = 99

second = 0
try:
    try:
        second = second + 1
    except ValueError:
        second = second + 100
    else:
        second = second + 2
    finally:
        second = second + 4
except ValueError:
    second = 99

third = 0
try:
    try:
        third = third + 1
        raise TypeError
    except ValueError:
        third = third + 100
    finally:
        third = third + 2
except TypeError:
    third = third + 4


def finalizer_overrides_handler_return():
    try:
        raise ValueError
    except ValueError:
        return 1
    finally:
        return 2


fourth = 0
try:
    try:
        raise ValueError
    except ValueError:
        fourth = fourth + 1
    finally:
        raise TypeError
except TypeError:
    fourth = fourth + 2

result = (
    first == 7
    and second == 7
    and third == 7
    and finalizer_overrides_handler_return() == 2
    and fourth == 3
)
assert result
result
