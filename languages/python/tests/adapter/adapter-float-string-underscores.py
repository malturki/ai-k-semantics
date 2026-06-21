result = float("1_000.25") == 1000.25
result = result and float("1.2_5") == 1.25
result = result and float("+10_0.") == 100.0
result = result and float(".1_25") == 0.125
result = result and float("1.2_5e0_2") == 125.0
result = result and float(" -1_0.2_5e+1 ") == -102.5
result = result and float("1e0_3") == 1000.0

assert result
result
