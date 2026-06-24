r = range(2, 7)
s = slice(1, 5, 2)
z = 1 + 2j

result = hasattr(r, "start")
result = result and hasattr(r, "stop")
result = result and hasattr(r, "step")
result = result and hasattr(s, "start")
result = result and hasattr(s, "stop")
result = result and hasattr(s, "step")
result = result and hasattr(z, "real")
result = result and hasattr(z, "imag")
result = result and hasattr(3, "real")
result = result and hasattr(3, "imag")
result = result and hasattr(3, "numerator")
result = result and hasattr(3, "denominator")
result = result and hasattr(True, "real")
result = result and hasattr(False, "imag")
result = result and hasattr(1.5, "real")
result = result and hasattr(1.5, "imag")
result = result and not hasattr(r, "missing")
result = result and not hasattr(s, "missing")
result = result and not hasattr(z, "missing")
result = result and not hasattr(3, "missing")

object_eval_error = False
try:
    hasattr(1 // 0, "real")
except ZeroDivisionError:
    object_eval_error = True

result = result and object_eval_error
assert result
result
