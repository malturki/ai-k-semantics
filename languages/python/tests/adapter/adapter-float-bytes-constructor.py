result = float(b"  -1.25\n") == -1.25
result = result and float(b"+1_2.5_0e+1") == 125.0
result = result and float(b"Infinity") == float("inf")
result = result and float(b"-inf") == float("-Infinity")
result = result and float(b"nan") != float(b"nan")
assert result
result
