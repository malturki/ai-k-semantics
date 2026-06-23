caught_primary = False
wrong_cause = False
try:
    raise ValueError from TypeError
except TypeError:
    wrong_cause = True
except ValueError:
    caught_primary = True

caught_call = False
try:
    raise KeyError() from RuntimeError()
except KeyError:
    caught_call = True

finally_seen = False
caught_finally = False
try:
    try:
        raise LookupError from RuntimeError
    finally:
        finally_seen = True
except LookupError:
    caught_finally = finally_seen

result = caught_primary and not wrong_cause and caught_call and caught_finally
assert result
result
