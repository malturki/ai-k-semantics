result = abs(-0.0) == 0.0
result = result and abs(0.0) == 0.0
result = result and repr(abs(float("inf"))) == "inf"
result = result and repr(abs(float("-inf"))) == "inf"
result = result and repr(abs(float("nan"))) == "nan"
assert result
result
