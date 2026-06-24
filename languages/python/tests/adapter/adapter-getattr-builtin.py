r = range(2, 7)
s = slice(1, 5, 2)
z = 1 + 2j

result = getattr(r, "start") == 2
result = result and getattr(r, "stop") == 7
result = result and getattr(r, "step") == 1
result = result and getattr(range(1, 8, 2), "step") == 2
result = result and getattr(s, "start") == 1
result = result and getattr(s, "stop") == 5
result = result and getattr(s, "step") == 2
result = result and getattr(slice(4), "start") is None
result = result and getattr(slice(4), "stop") == 4
result = result and getattr(slice(4), "step") is None
result = result and getattr(z, "real") == 1.0
result = result and getattr(z, "imag") == 2.0
result = result and getattr(3, "real") == 3
result = result and getattr(3, "imag") == 0
result = result and getattr(3, "numerator") == 3
result = result and getattr(3, "denominator") == 1
result = result and getattr(True, "real") == 1
result = result and getattr(False, "imag") == 0
result = result and getattr(1.5, "real") == 1.5
result = result and getattr(1.5, "imag") == 0.0
result = result and getattr(range(1), "missing", 7) == 7

missing_error = False
try:
    getattr(range(1), "missing")
except AttributeError:
    missing_error = True

result = result and missing_error

default_eval_error = False
try:
    getattr(range(1), "start", 1 // 0)
except ZeroDivisionError:
    default_eval_error = True

result = result and default_eval_error
assert result
result
