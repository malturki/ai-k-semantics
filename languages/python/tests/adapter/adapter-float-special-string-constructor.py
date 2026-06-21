result = float("inf") == float("Infinity")
result = result and float("+INF") == float("infinity")
result = result and float("-inf") == -float("inf")
result = result and float(" \t-InFiNiTy\n") == -float("inf")
result = result and float("nan") != float("nan")
result = result and float("+NaN") != float("-nan")

assert result
result
