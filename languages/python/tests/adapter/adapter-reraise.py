caught_basic = False
try:
    try:
        raise ValueError
    except ValueError:
        raise
except ValueError:
    caught_basic = True

caught_inner = False
caught_outer = False
try:
    raise ValueError
except ValueError:
    try:
        raise TypeError
    except TypeError:
        try:
            raise
        except TypeError:
            caught_inner = True
    try:
        raise
    except ValueError:
        caught_outer = True

caught_as = False
try:
    try:
        raise KeyError
    except KeyError as exc:
        raise
except KeyError:
    caught_as = True


def helper():
    raise


caught_helper = False
try:
    try:
        raise LookupError
    except LookupError:
        helper()
except LookupError:
    caught_helper = True

caught_runtime = False
try:
    raise
except RuntimeError:
    caught_runtime = True

result = caught_basic and caught_inner and caught_outer and caught_as and caught_helper and caught_runtime
assert result
result
