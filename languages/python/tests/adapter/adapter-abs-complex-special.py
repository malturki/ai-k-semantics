inf = float("inf")
neg_inf = float("-inf")
nan = float("nan")

result = repr(abs(complex(inf, 1.0))) == "inf"
result = result and repr(abs(complex(neg_inf, 1.0))) == "inf"
result = result and repr(abs(complex(1.0, inf))) == "inf"
result = result and repr(abs(complex(nan, 2.0))) == "nan"
result = result and repr(abs(complex(2.0, nan))) == "nan"
result = result and repr(abs(complex(nan, inf))) == "inf"
result = result and repr(abs(complex(neg_inf, nan))) == "inf"
result = result and repr(abs(complex(nan, nan))) == "nan"
assert result
result
