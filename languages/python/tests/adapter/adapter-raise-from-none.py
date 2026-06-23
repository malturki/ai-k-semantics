caught_name = False
try:
    raise ValueError from None
except ValueError:
    caught_name = True

caught_call = False
try:
    raise TypeError() from None
except TypeError:
    caught_call = True

wrong_first = False
right_second = False
try:
    raise KeyError from None
except ValueError:
    wrong_first = True
except KeyError:
    right_second = True

finally_seen = False
caught_finally = False
try:
    try:
        raise RuntimeError from None
    finally:
        finally_seen = True
except RuntimeError:
    caught_finally = finally_seen

result = caught_name and caught_call and right_second and not wrong_first and caught_finally
assert result
result
