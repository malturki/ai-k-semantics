caught_string = False
seen_arg = False
try:
    raise ValueError((seen_arg := True))
except ValueError:
    caught_string = seen_arg

wrong_first = False
right_second = False
try:
    raise TypeError(1, "bad")
except ValueError:
    wrong_first = True
except TypeError:
    right_second = True

caught_as = False
try:
    try:
        raise KeyError("missing")
    except KeyError as exc:
        raise
except KeyError:
    caught_as = True

caught_from_none = False
try:
    raise RuntimeError("hidden") from None
except RuntimeError:
    caught_from_none = True

caught_from_cause = False
try:
    raise LookupError("outer") from ValueError("inner")
except LookupError:
    caught_from_cause = True

result = caught_string and right_second and not wrong_first and caught_as and caught_from_none and caught_from_cause
assert result
result
